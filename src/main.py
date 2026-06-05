import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow
from gui.resources import main_rc

_ = main_rc


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Synth")
    app.setOrganizationName("Synth")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
