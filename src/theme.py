from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QStyleFactory

THEME_LIGHT = "light"
THEME_DARK = "dark"
THEME_SYSTEM = "system"
DEFAULT_THEME = THEME_LIGHT
THEMES = (THEME_LIGHT, THEME_DARK, THEME_SYSTEM)

THEME_LABELS = {
    THEME_LIGHT: "Light",
    THEME_DARK: "Dark",
    THEME_SYSTEM: "System",
}


def apply_theme(theme: str) -> None:
    app = QApplication.instance()
    if app is None:
        return

    style = QStyleFactory.create("Fusion")
    if style is not None:
        app.setStyle(style)

    if theme == THEME_DARK:
        app.setPalette(_dark_palette())
    elif theme == THEME_SYSTEM:
        app.setPalette(app.style().standardPalette())
    else:
        app.setPalette(_light_palette())


def _light_palette() -> QPalette:
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#f5f5f5"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("#111111"))
    palette.setColor(QPalette.ColorRole.Base, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#eeeeee"))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#111111"))
    palette.setColor(QPalette.ColorRole.Text, QColor("#111111"))
    palette.setColor(QPalette.ColorRole.Button, QColor("#f0f0f0"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("#111111"))
    palette.setColor(QPalette.ColorRole.BrightText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Highlight, QColor("#2a82da"))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))
    return palette


def _dark_palette() -> QPalette:
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#202124"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("#f1f3f4"))
    palette.setColor(QPalette.ColorRole.Base, QColor("#151719"))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#25282c"))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#2b2f33"))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#f1f3f4"))
    palette.setColor(QPalette.ColorRole.Text, QColor("#f1f3f4"))
    palette.setColor(QPalette.ColorRole.Button, QColor("#2b2f33"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("#f1f3f4"))
    palette.setColor(QPalette.ColorRole.BrightText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Highlight, QColor("#4c8eda"))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))
    return palette
