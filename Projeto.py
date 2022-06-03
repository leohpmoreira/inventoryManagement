from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton
import sys
import Logs
import sqlite3


class ExampleApp(QtWidgets.QMainWindow, Logs.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_login.clicked.connect(lambda: self.login())
        self.pushButton_close.clicked.connect(lambda: self.hide())

    def login(self):
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        user = self.lineEdit_user.text()
        pwd = self.lineEdit_password.text()
        print(user, pwd)
        cur.execute("SELECT * FROM Login WHERE UserID = :login AND Password = :passwd",
                    {'login': user, 'passwd': pwd})
        if not cur.fetchone():
            print("Login failed")
            self.pushButton_close.setVisible(True)
            self.label_erro.setVisible(True)
            self.frame_erro.setVisible(True)
            # show error
        else:
            print("Welcome")
            # go to menu

    def hide(self):
        self.pushButton_close.setVisible(False)
        self.label_erro.setVisible(False)
        self.frame_erro.setVisible(False)


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
