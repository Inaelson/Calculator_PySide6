import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from widgets import MainWindow, Info, Display, ButtonsGrid
from variables import WINDOW_ICON_PATH, setupTheme

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    theme = setupTheme()
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info()
    window.addWidgetToVlayout(info)

    # Display
    display = Display()
    window.addWidgetToVlayout(display)

    # Grid
    buttonsgrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsgrid)

    # Execute all
    window.adjustFixedSize()
    window.show()
    app.exec()
