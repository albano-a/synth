import os
import subprocess
import sys
from pathlib import Path

# Must be set before any pyqtgraph import
os.environ.setdefault("PYQTGRAPH_QT_LIB", "PySide6")

_SRC = Path(__file__).parent


def _ensure_ui() -> None:
    if hasattr(sys, "_MEIPASS"):
        return
    src = _SRC / "gui" / "qt" / "SynthMainWindow.ui"
    dst = _SRC / "gui" / "qt" / "ui_SynthMainWindow.py"
    if not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime:
        subprocess.run(["pyside6-uic", str(src), "-o", str(dst)], check=True)
    if dst.exists():
        lines = dst.read_text(encoding="utf-8").splitlines()
        fixed_lines = [
            "from gui.resources import main_rc"
            if line.strip() in {"import main_rc", "import gui.rsources.main_rc"}
            else line
            for line in lines
        ]
        dst.write_text("\n".join(fixed_lines) + "\n", encoding="utf-8")


def _ensure_rc() -> None:
    if hasattr(sys, "_MEIPASS"):
        return
    src = _SRC / "gui" / "resources" / "main.qrc"
    dst = _SRC / "gui" / "resources" / "main_rc.py"
    if not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime:
        subprocess.run(["pyside6-rcc", str(src), "-o", str(dst)], check=True)


_ensure_ui()
_ensure_rc()

from PySide6.QtWidgets import QApplication  # noqa: E402

from gui.resources import main_rc  # noqa: E402 — registers Qt resources
from main_window import MainWindow  # noqa: E402
from theme import DEFAULT_THEME, apply_theme  # noqa: E402

_ = main_rc


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Synth")
    app.setOrganizationName("Synth")
    apply_theme(DEFAULT_THEME)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
