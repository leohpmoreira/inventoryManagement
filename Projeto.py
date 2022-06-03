from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton
import sys
import loginWindow


class initializeWindow(QtWidgets.QMainWindow, loginWindow.main_window):
    def __init__(self, parent=None):
        super(initializeWindow, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = initializeWindow()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
