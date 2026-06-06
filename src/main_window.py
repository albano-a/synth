from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import QSettings
from PySide6.QtGui import QAction, QActionGroup, QIcon
from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow,
    QMenu,
    QMessageBox,
    QVBoxLayout,
)

from core import las_loader, seismic, wavelet
from gui.qt.ui_SynthMainWindow import Ui_MainWindow
from theme import DEFAULT_THEME, THEME_DARK, THEME_LABELS, THEMES, apply_theme

_DELIMITERS: dict[str, str | None] = {
    "space": None,
    "tab": "\t",
    "comma": ",",
    "semicolon": ";",
}

_VP_MNEMONICS = ["VP", "VELP", "VEL", "VELI", "VPHI", "PWAVE", "P_WAVE"]
_RHOB_MNEMONICS = ["RHOB", "DENS", "DEN", "RHOZ", "DENB", "ZDEN", "DENSITY"]

_TRACK_COLORS = {
    "vp": "b",
    "rhob": "r",
    "ai": "g",
    "refl": "k",
    "synth": "k",
}
_GRID_ALPHA = 0.15
_THEME_SETTINGS_KEY = "theme"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Synth")
        self.setWindowIcon(QIcon(":/icons/icons/logo.png"))

        self._settings = QSettings("Synth", "Synth")

        self._las = None
        self._wavelet: np.ndarray | None = None
        self._vp = self._rhob = self._ai = self._refl = self._synth = None
        self._depth = self._depth_refl = self._twt = None

        self._setup_display()
        self._setup_wavelet_preview()
        self._setup_menus()
        self._connect_signals()
        self._apply_theme()
        self.mwFileTypeRadioButton.setChecked(True)

    # ------------------------------------------------------------------ setup

    def _setup_display(self):
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")
        layout = QVBoxLayout(self.mwDisplayWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        self._display = pg.GraphicsLayoutWidget()
        layout.addWidget(self._display)
        self._setup_tracks()

    def _setup_tracks(self):
        self._track_vp = self._display.addPlot(title="Vp")
        self._track_rhob = self._display.addPlot(title="RHOB")
        self._track_ai = self._display.addPlot(title="AI")
        self._track_refl = self._display.addPlot(title="Reflectivity")
        self._track_synth = self._display.addPlot(title="Synthetic")

        self._all_tracks = [
            self._track_vp,
            self._track_rhob,
            self._track_ai,
            self._track_refl,
            self._track_synth,
        ]

        for track in self._all_tracks[1:]:
            track.setYLink(self._track_vp)
            track.getAxis("left").hide()

        for track in self._all_tracks:
            track.invertY(True)
            track.showGrid(x=True, y=True, alpha=_GRID_ALPHA)

        self._track_vp.getAxis("left").setLabel("Depth (m)")

    def _setup_wavelet_preview(self):
        layout = QVBoxLayout(self.mwWaveletPreviewWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        self._wavelet_plot = pg.PlotWidget()
        self._wavelet_plot.setBackground("w")
        self._wavelet_plot.showGrid(x=False, y=True, alpha=0.3)
        self._wavelet_plot.getAxis("bottom").setLabel("Sample")
        self._wavelet_plot.getAxis("left").setLabel("Amplitude")
        layout.addWidget(self._wavelet_plot)

    def _setup_menus(self):
        edit_menu = QMenu("Edit", self)
        self.menubar.insertMenu(self.menuView.menuAction(), edit_menu)
        self._action_clear_plots = QAction("Clear Plots", self)
        edit_menu.addAction(self._action_clear_plots)
        edit_menu.addSeparator()
        self._setup_theme_menu(edit_menu)

        self._recent_menu = QMenu("Recent Files", self)
        self.menuFile.insertMenu(self.actionRecent_Files, self._recent_menu)
        self.menuFile.removeAction(self.actionRecent_Files)
        self._refresh_recent_menu()

    def _setup_theme_menu(self, edit_menu: QMenu):
        theme_menu = QMenu("Theme", self)
        edit_menu.addMenu(theme_menu)

        self._theme_action_group = QActionGroup(self)
        self._theme_action_group.setExclusive(True)
        self._theme_actions: dict[str, QAction] = {}
        current_theme = self._current_theme()

        for theme in THEMES:
            action = QAction(THEME_LABELS[theme], self)
            action.setCheckable(True)
            action.setChecked(theme == current_theme)
            action.triggered.connect(
                lambda checked, selected_theme=theme: self._on_theme_selected(
                    selected_theme, checked
                )
            )
            self._theme_action_group.addAction(action)
            theme_menu.addAction(action)
            self._theme_actions[theme] = action

    def _connect_signals(self):
        self.actionOpen_LAS.triggered.connect(self._on_open_las)
        self.actionOpen_Wavelet.triggered.connect(self._on_open_wavelet)
        self.actionExit.triggered.connect(self.close)
        self.actionPNG.triggered.connect(lambda: self._on_export_figure("png"))
        self.actionPDF.triggered.connect(lambda: self._on_export_figure("pdf"))
        self.actionCSV.triggered.connect(self._on_export_csv)
        self.actionShow_Hide_Controls_Panel.triggered.connect(self._toggle_controls_panel)
        self.actionAbout_Synth.triggered.connect(self._on_about)
        self._action_clear_plots.triggered.connect(self._on_clear_plots)

        self.mwBrowseButton.clicked.connect(self._on_open_las)

        self.mwRickerTypeRadioButton.toggled.connect(
            lambda checked: self.mwWaveletTypeStackedWidget.setCurrentIndex(0) if checked else None
        )
        self.mwOrmsbyTypeRadioButton.toggled.connect(
            lambda checked: self.mwWaveletTypeStackedWidget.setCurrentIndex(1) if checked else None
        )
        self.mwFileTypeRadioButton.toggled.connect(
            lambda checked: self.mwWaveletTypeStackedWidget.setCurrentIndex(2) if checked else None
        )

        self.mwWaveletFilePathBrowseButton.clicked.connect(self._on_browse_wavelet_file)
        self.mwRickerGenerateButton.clicked.connect(self._on_generate_ricker)
        self.mwGenerateOrmsbyButton.clicked.connect(self._on_generate_ormsby)
        self.mwFileReadButton.clicked.connect(self._on_read_wavelet_file)
        self.mwComputeButton.clicked.connect(self._on_compute)
        self.mwExportResultsButton.clicked.connect(self._on_export_csv)

    def _current_theme(self) -> str:
        theme = self._settings.value(_THEME_SETTINGS_KEY, DEFAULT_THEME)
        return theme if theme in THEMES else DEFAULT_THEME

    def _on_theme_selected(self, theme: str, checked: bool):
        if not checked:
            return
        self._settings.setValue(_THEME_SETTINGS_KEY, theme)
        self._apply_theme(theme)

    def _apply_theme(self, theme: str | None = None):
        theme = theme or self._current_theme()
        apply_theme(theme)
        self._apply_plot_theme(theme)

    def _apply_plot_theme(self, theme: str):
        dark = theme == THEME_DARK
        background = "#151719" if dark else "w"
        foreground = "#f1f3f4" if dark else "k"
        grid_alpha = 0.22 if dark else _GRID_ALPHA

        pg.setConfigOption("background", background)
        pg.setConfigOption("foreground", foreground)
        self._display.setBackground(background)
        self._wavelet_plot.setBackground(background)

        for track in self._all_tracks:
            track.showGrid(x=True, y=True, alpha=grid_alpha)
            for axis_name in ("left", "bottom"):
                axis = track.getAxis(axis_name)
                axis.setPen(pg.mkPen(foreground))
                axis.setTextPen(pg.mkPen(foreground))

        for axis_name in ("left", "bottom"):
            axis = self._wavelet_plot.getAxis(axis_name)
            axis.setPen(pg.mkPen(foreground))
            axis.setTextPen(pg.mkPen(foreground))

        if self._wavelet is not None:
            self._update_wavelet_preview()
        if self._synth is not None:
            self._plot_tracks()

    def _plot_foreground(self) -> str:
        return "#f1f3f4" if self._current_theme() == THEME_DARK else "k"

    def _plot_fill(self):
        return pg.mkBrush(241, 243, 244, 150) if self._current_theme() == THEME_DARK else pg.mkBrush(0, 0, 0, 180)

    # ------------------------------------------------------------------ recent files

    def _save_recent(self, path: str):
        recent: list = self._settings.value("recent_files", []) or []
        if path in recent:
            recent.remove(path)
        recent.insert(0, path)
        self._settings.setValue("recent_files", recent[:5])
        self._refresh_recent_menu()

    def _refresh_recent_menu(self):
        self._recent_menu.clear()
        recent: list = self._settings.value("recent_files", []) or []
        if not recent:
            placeholder = QAction("(empty)", self)
            placeholder.setEnabled(False)
            self._recent_menu.addAction(placeholder)
            return
        for path in recent:
            action = QAction(Path(path).name, self)
            action.setToolTip(path)
            action.triggered.connect(lambda checked, p=path: self._open_recent(p))
            self._recent_menu.addAction(action)
        self._recent_menu.addSeparator()
        clear_action = QAction("Clear Recent", self)
        clear_action.triggered.connect(self._clear_recent)
        self._recent_menu.addAction(clear_action)

    def _open_recent(self, path: str):
        if not Path(path).exists():
            self._warn(f"File not found:\n{path}")
            return
        self.mwLasFileInput.setText(path)
        self._load_las(path)

    def _clear_recent(self):
        self._settings.remove("recent_files")
        self._refresh_recent_menu()

    # ------------------------------------------------------------------ helpers

    def _warn(self, msg: str):
        QMessageBox.warning(self, "Synth", msg)

    def _error(self, title: str, exc: Exception):
        QMessageBox.critical(self, title, str(exc))

    @staticmethod
    def _best_match(names: list[str], candidates: list[str]) -> str | None:
        upper = [n.upper() for n in names]
        for c in candidates:
            if c.upper() in upper:
                return names[upper.index(c.upper())]
        return None

    def _clear_track(self, track: pg.PlotItem):
        track.clear()
        alpha = 0.22 if self._current_theme() == THEME_DARK else _GRID_ALPHA
        track.showGrid(x=True, y=True, alpha=alpha)

    # ------------------------------------------------------------------ slots

    def _on_open_las(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open LAS File", "", "LAS Files (*.las *.LAS)")
        if path:
            self.mwLasFileInput.setText(path)
            self._load_las(path)

    def _load_las(self, path: str):
        try:
            self._las = las_loader.load(path)
            names = las_loader.curve_names(self._las)
            dep = las_loader.depth(self._las)

            self.mwVpCurveCombobox.clear()
            self.mwRhobCurveCombobox.clear()
            self.mwVpCurveCombobox.addItems(names)
            self.mwRhobCurveCombobox.addItems(names)

            vp_match = self._best_match(names, _VP_MNEMONICS)
            if vp_match:
                self.mwVpCurveCombobox.setCurrentText(vp_match)

            rhob_match = self._best_match(names, _RHOB_MNEMONICS)
            if rhob_match:
                self.mwRhobCurveCombobox.setCurrentText(rhob_match)

            self.mwDepthTopInput.setText(f"{dep.min():.2f}")
            self.mwDepthBottomInput.setText(f"{dep.max():.2f}")
            self._save_recent(path)
            self.statusbar.showMessage(f"Loaded: {Path(path).name}", 4000)
        except Exception as exc:
            self._error("Error loading LAS", exc)

    def _on_open_wavelet(self):
        self.mwFileTypeRadioButton.setChecked(True)
        self._on_browse_wavelet_file()

    def _on_browse_wavelet_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open Wavelet File", "", "Text Files (*.txt *.csv);;All Files (*)"
        )
        if path:
            self.mwWaveletFilePathInput.setText(path)

    def _toggle_controls_panel(self):
        self.dockWidget.setVisible(not self.dockWidget.isVisible())

    def _on_about(self):
        QMessageBox.about(
            self,
            "About Synth",
            "Synth v0.1.0\nSynthetic seismogram generator for geophysicists.",
        )

    def _on_clear_plots(self):
        for track in self._all_tracks:
            self._clear_track(track)
        self._vp = self._rhob = self._ai = self._refl = self._synth = None
        self._depth = self._depth_refl = self._twt = None
        self.statusbar.showMessage("Plots cleared.", 3000)

    def _on_generate_ricker(self):
        try:
            f = float(self.mwRickerPeakFreqInput.text())
            n = int(self.mwRickerSamplesInput.text())
            dt = float(self.mwRickerTimeInput.text()) / 1000.0
            self._wavelet = wavelet.ricker(f, n, dt)
            self._update_wavelet_preview()
            self.statusbar.showMessage(f"Ricker wavelet: {f} Hz, {n} samples", 3000)
        except ValueError as exc:
            self._error("Ricker Wavelet", exc)

    def _on_generate_ormsby(self):
        try:
            f1 = float(self.mwOrmsbyLowCutoffFreqInput.text())
            f2 = float(self.mwOrmsbyLowFreqInput.text())
            f3 = float(self.mwOrmsbyHighFreqInput.text())
            f4 = float(self.mwOrmsbyHighCutoffFreqInput.text())
            n = int(self.mwOrmsbySamplesInput.text())
            dt = float(self.mwOrmsbyTimeInput.text()) / 1000.0
            self._wavelet = wavelet.ormsby(f1, f2, f3, f4, n, dt)
            self._update_wavelet_preview()
            self.statusbar.showMessage(f"Ormsby wavelet: {f1}/{f2}/{f3}/{f4} Hz, {n} samples", 3000)
        except ValueError as exc:
            self._error("Ormsby Wavelet", exc)

    def _on_read_wavelet_file(self):
        path = self.mwWaveletFilePathInput.text().strip()
        if not path:
            self._warn("Select a wavelet file first.")
            return
        try:
            skiprows = int(self.mwWaveletFileSkiprowsInput.text() or 0)
            delimiter = _DELIMITERS[self.mwWaveletFileDelimiterCombobox.currentText()]
            self._wavelet = wavelet.from_file(path, skiprows=skiprows, delimiter=delimiter)
            self._update_wavelet_preview()
            self.statusbar.showMessage(f"Wavelet loaded: {len(self._wavelet)} samples", 3000)
        except Exception as exc:
            self._error("Error reading wavelet file", exc)

    def _update_wavelet_preview(self):
        self._wavelet_plot.clear()
        if self._wavelet is None:
            return
        n = len(self._wavelet)
        x = np.arange(n) - n // 2
        self._wavelet_plot.plot(x, self._wavelet, pen=pg.mkPen("b", width=2))
        self._wavelet_plot.addLine(
            y=0,
            pen=pg.mkPen(
                self._plot_foreground(), width=0.5, style=pg.QtCore.Qt.PenStyle.DashLine
            ),
        )

    def _on_compute(self):
        if self._las is None:
            self._warn("Load a LAS file first.")
            return
        if self._wavelet is None:
            self._warn("Generate or load a wavelet first.")
            return

        vp_name = self.mwVpCurveCombobox.currentText()
        rhob_name = self.mwRhobCurveCombobox.currentText()
        if not vp_name or not rhob_name:
            self._warn("Select Vp and RHOB curves.")
            return

        try:
            dep = las_loader.depth(self._las)
            vp = las_loader.get_curve(self._las, vp_name)
            rhob = las_loader.get_curve(self._las, rhob_name)

            mask = np.ones(len(dep), dtype=bool)
            top = self.mwDepthTopInput.text().strip()
            bot = self.mwDepthBottomInput.text().strip()
            if top:
                mask &= dep >= float(top)
            if bot:
                mask &= dep <= float(bot)

            dep, vp, rhob = dep[mask], vp[mask], rhob[mask]
            valid = ~(np.isnan(vp) | np.isnan(rhob))
            dep, vp, rhob = dep[valid], vp[valid], rhob[valid]

            ai = seismic.acoustic_impedance(vp, rhob)
            refl = seismic.reflectivity(ai)
            synth = seismic.synthetic(refl, self._wavelet)
            dep_refl = dep[:-1]

            dz = np.diff(dep)
            twt = np.cumsum(2.0 * dz / vp[:-1]) * 1000.0  # ms

            self._depth, self._vp, self._rhob = dep, vp, rhob
            self._ai, self._refl, self._synth = ai, refl, synth
            self._depth_refl, self._twt = dep_refl, twt

            self._plot_tracks()
            self.statusbar.showMessage("Done.", 3000)
        except Exception as exc:
            self._error("Compute error", exc)

    def _plot_tracks(self):
        self._clear_track(self._track_vp)
        self._track_vp.plot(self._vp, self._depth, pen=pg.mkPen("b", width=2))

        self._clear_track(self._track_rhob)
        self._track_rhob.plot(self._rhob, self._depth, pen=pg.mkPen("r", width=2))

        self._clear_track(self._track_ai)
        self._track_ai.plot(self._ai, self._depth, pen=pg.mkPen("g", width=2))

        self._clear_track(self._track_refl)
        self._track_refl.plot(
            self._refl, self._depth_refl, pen=pg.mkPen(self._plot_foreground(), width=2)
        )

        self._clear_track(self._track_synth)
        self._track_synth.plot(
            self._synth, self._depth_refl, pen=pg.mkPen(self._plot_foreground(), width=2)
        )
        pos_curve = self._track_synth.plot(np.maximum(self._synth, 0.0), self._depth_refl, pen=None)
        zero_curve = self._track_synth.plot(np.zeros_like(self._synth), self._depth_refl, pen=None)
        self._track_synth.addItem(pg.FillBetweenItem(zero_curve, pos_curve, brush=self._plot_fill()))

        for track in self._all_tracks:
            track.getViewBox().enableAutoRange(pg.ViewBox.XAxis, True)

    def _on_export_csv(self):
        if self._synth is None:
            self._warn("Compute synthetic first.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export Synthetic", "", "CSV Files (*.csv)")
        if not path:
            return
        np.savetxt(
            path,
            np.column_stack([self._depth_refl, self._twt, self._synth]),
            delimiter=",",
            header="depth_m,twt_ms,amplitude",
            comments="",
        )
        self.statusbar.showMessage(f"Saved: {path}", 3000)

    def _on_export_figure(self, fmt: str):
        if self._synth is None:
            self._warn("Compute synthetic first.")
            return
        ext = "PNG Files (*.png)" if fmt == "png" else "PDF Files (*.pdf)"
        path, _ = QFileDialog.getSaveFileName(self, "Export Figure", "", ext)
        if not path:
            return

        fig, axes = plt.subplots(1, 5, figsize=(14, 10), sharey=True)
        pairs = [
            (axes[0], self._vp, self._depth, "Vp", "blue"),
            (axes[1], self._rhob, self._depth, "RHOB", "red"),
            (axes[2], self._ai, self._depth, "AI", "green"),
            (axes[3], self._refl, self._depth_refl, "Reflectivity", "black"),
        ]
        for ax, data, dep, title, color in pairs:
            ax.plot(data, dep, color=color, linewidth=0.8)
            ax.set_title(title)
            ax.invert_yaxis()
            ax.grid(True, alpha=0.2)

        axes[4].plot(self._synth, self._depth_refl, "k", linewidth=0.8)
        axes[4].fill_betweenx(
            self._depth_refl, 0, self._synth, where=self._synth > 0, facecolor="k"
        )
        axes[4].set_title("Synthetic")
        axes[4].invert_yaxis()
        axes[4].grid(True, alpha=0.2)

        axes[0].set_ylabel("Depth (m)")
        plt.tight_layout()
        plt.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        self.statusbar.showMessage(f"Saved: {path}", 3000)
