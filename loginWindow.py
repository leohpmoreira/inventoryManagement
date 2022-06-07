# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Logs.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from menuWindow import menu_window
from menuSecundario import menuSecundario_window

current = "empty"

class main_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 881)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_erro = QtWidgets.QFrame(self.top_bar)
        self.frame_erro.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_erro.setStyleSheet("background-color: rgb(255, 85, 127);\n"
                                      "border-radius: 10px;")
        self.frame_erro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_erro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erro.setObjectName("frame_erro")
        self.frame_erro.setVisible(False)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_erro)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_erro = QtWidgets.QLabel(self.frame_erro)
        self.label_erro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erro.setObjectName("label_erro")
        self.label_erro.setVisible(False)
        self.horizontalLayout_3.addWidget(self.label_erro)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_erro)
        self.pushButton_close.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setStyleSheet("QPushButton {\n"
                                            "    border-radius: 5px;    \n"
                                            "    background-image: url(:/Close_Image/Images/cil-x.png);\n"
                                            "    background-position: center;\n"
                                            "    background-color: rgb(255, 0, 127);\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(6, 21, 60);\n"
                                            "    color: rgb(200, 200, 200);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    color: rgb(200, 200, 200);\n"
                                            "}")
        self.pushButton_close.setText("")
        self.pushButton_close.setVisible(False)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_3.addWidget(self.pushButton_close)
        self.horizontalLayout_2.addWidget(self.frame_erro)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMinimumSize(QtCore.QSize(0, 0))
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("background-color: rgb(6, 21, 60);\n"
                                      "border-radius: 20px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.frame = QtWidgets.QFrame(self.login_area)
        self.frame.setGeometry(QtCore.QRect(110, 15, 231, 100))
        self.frame.setStyleSheet("background-image: url(:/Logo/LOGOFE.png);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.avatar = QtWidgets.QFrame(self.login_area)
        self.avatar.setGeometry(QtCore.QRect(110, 100, 231, 201))
        self.avatar.setStyleSheet("QFrame {\n"
                                  "    background-image: url(:/Avatar/AAAA.png);\n"
                                  "    background-position: center;\n"
                                  "    border-radius: 50px;\n"
                                  "    border: 10px solid rgb(245, 222, 179)\n"
                                  "}")
        self.avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setObjectName("avatar")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_user.setGeometry(QtCore.QRect(85, 320, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
                                         "    border: 3px solid rgb(245, 222, 179);\n"
                                         "    border-radius: 5px;\n"
                                         "    padding: 15px;\n"
                                         "    background-color:rgb(249, 234, 195);\n"
                                         "    color: rgb(45, 45, 45);\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 3px solid rgb(55, 55, 55);\n"
                                         "}\n"
                                         "QLineEdit:focus {\n"
                                         "    border: 3px solid rgb(135, 206, 250);\n"
                                         "    color: rgb(45, 45, 45);\n"
                                         "}")
        self.lineEdit_user.setMaxLength(45)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(85, 375, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
                                             "    border: 3px solid rgb(245, 222, 179);\n"
                                             "    border-radius: 5px;\n"
                                             "    padding: 15px;\n"
                                             "    background-color:rgb(249, 234, 195);\n"
                                             "    color: rgb(45, 45, 45);\n"
                                             "}\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 3px solid rgb(55, 55, 55);\n"
                                             "}\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 3px solid rgb(135, 206, 250);\n"
                                             "    color: rgb(45, 45, 45);\n"
                                             "}")
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area, clicked=lambda: self.login())
        self.pushButton_login.setGeometry(QtCore.QRect(85, 440, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton{    \n"
                                            "    border: 3px solid rgb(245, 222, 179);\n"
                                            "    border-radius: 25px;\n"
                                            "    background-color:rgb(249, 234, 195);\n"
                                            "    color: rgb(45, 45, 45);\n"
                                            "}\n"
                                            "QPushButton:hover{    \n"
                                            "    border: 3px solid rgb(55, 55, 55);\n"
                                            "}\n"
                                            "QPushButton:pressed{    \n"
                                            "    background-color: rgb(135, 206, 250);\n"
                                            "    color: rgb(45, 45, 45);\n"
                                            "}")
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.botom_bar = QtWidgets.QFrame(self.centralwidget)
        self.botom_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.botom_bar.setStyleSheet("color: rgb(15, 15, 15);")
        self.botom_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.botom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botom_bar.setObjectName("botom_bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.botom_bar)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_marca = QtWidgets.QLabel(self.botom_bar)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_marca.setFont(font)
        self.label_marca.setStyleSheet("\n"
                                       "color: rgb(75, 75, 75);")
        self.label_marca.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_marca.setObjectName("label_marca")
        self.verticalLayout_2.addWidget(self.label_marca)
        self.verticalLayout.addWidget(self.botom_bar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_close.clicked.connect(lambda: self.hide_error())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_erro.setText(_translate("MainWindow", "Error"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "USER"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "SENHA"))
        self.pushButton_login.setText(_translate("MainWindow", "ENTRAR"))
        self.label_marca.setText(_translate("MainWindow", "Created By: ;Code Inc."))

    def login(self):
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        user = self.lineEdit_user.text()
        pwd = self.lineEdit_password.text()
        print("Tentativa de login com dados: ", user, pwd)
        cur.execute("SELECT * FROM Login WHERE UserID = :login AND Password = :passwd",
                    {'login': self.lineEdit_user.text(), 'passwd': pwd})
        tipo = cur.fetchone()
        if not tipo:
            print("Login failed")
            self.pushButton_close.setVisible(True)
            self.label_erro.setVisible(True)
            self.frame_erro.setVisible(True)
            # show error
        else:
            print("Welcome")
            global current
            current = user
            print(current)
            self.close()
            self.window = QtWidgets.QMainWindow()
            self.window.setFixedSize(QtCore.QSize(1000,500))
            if tipo[2].upper() == 'A':
                self.ui = menu_window()
            else:
                self.ui = menuSecundario_window()
            self.ui.setupUi(self.window)
            self.window.show()

            # go to menu

    def hide_error(self):
        self.pushButton_close.setVisible(False)
        self.label_erro.setVisible(False)
        self.frame_erro.setVisible(False)


import file_rc
