import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow, Info, Display
from variables import WINDOW_ICON_PATH, setupTheme

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    theme = setupTheme()
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('25.0 * 35.5')
    window.addWidgetToVlayout(info)

    # Display
    display = Display()
    window.addWidgetToVlayout(display)

    # Execute all
    window.adjustFixedSize()
    window.show()
    app.exec()
