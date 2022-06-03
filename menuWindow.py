from PyQt5 import QtCore, QtGui, QtWidgets
from newProduct import newProductWindow

class menu_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 605)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_top.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_top)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_toggle = QtWidgets.QPushButton(self.frame_top, clicked=lambda: self.side_menu())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_toggle.sizePolicy().hasHeightForWidth())
        self.Btn_toggle.setSizePolicy(sizePolicy)
        self.Btn_toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;")
        self.Btn_toggle.setObjectName("Btn_toggle")
        self.verticalLayout_2.addWidget(self.Btn_toggle)
        self.horizontalLayout.addWidget(self.frame_top)
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Btn_menu_1 = QtWidgets.QPushButton(self.frame_top_menus, clicked=lambda: self.new_product())
        self.Btn_menu_1.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_menu_1.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_menu_1.setObjectName("Btn_menu_1")
        self.verticalLayout_4.addWidget(self.Btn_menu_1)
        self.Btn_menu_2 = QtWidgets.QPushButton(self.frame_top_menus, clicked=lambda: self.delete_product())
        self.Btn_menu_2.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_menu_2.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_menu_2.setObjectName("Btn_menu_2")
        self.verticalLayout_4.addWidget(self.Btn_menu_2)
        self.Btn_menu_3 = QtWidgets.QPushButton(self.frame_top_menus, clicked=lambda: self.restock_product())
        self.Btn_menu_3.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_menu_3.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_menu_3.setObjectName("Btn_menu_3")
        self.verticalLayout_4.addWidget(self.Btn_menu_3)
        self.Btn_menu_4 = QtWidgets.QPushButton(self.frame_top_menus, clicked=lambda: self.remove_product())
        self.Btn_menu_4.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_menu_4.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_menu_4.setObjectName("Btn_menu_4")
        self.verticalLayout_4.addWidget(self.Btn_menu_4)
        self.Btn_menu_5 = QtWidgets.QPushButton(self.frame_top_menus, clicked=lambda: self.check_stock())
        self.Btn_menu_5.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_menu_5.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_menu_5.setObjectName("Btn_menu_5")
        self.verticalLayout_4.addWidget(self.Btn_menu_5)
        self.Btn_menu_6 = QtWidgets.QPushButton(self.frame_top_menus, clicked=lambda: self.transaction_history())
        self.Btn_menu_6.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_menu_6.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_menu_6.setObjectName("Btn_menu_6")
        self.verticalLayout_4.addWidget(self.Btn_menu_6)
        self.Btn_menu_7 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_7.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_menu_7.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_menu_7.setObjectName("Btn_menu_7")
        self.verticalLayout_4.addWidget(self.Btn_menu_7)
        self.Btn_menu_8 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_8.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_menu_8.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_menu_8.setObjectName("Btn_menu_8")
        self.verticalLayout_4.addWidget(self.Btn_menu_8)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PagesWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.PagesWidget.setObjectName("PagesWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.PagesWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.PagesWidget.addWidget(self.page_2)
        self.verticalLayout_5.addWidget(self.PagesWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_toggle.setText(_translate("MainWindow", "TOGGLE"))
        self.Btn_menu_1.setText(_translate("MainWindow", "CADASTRAR PRODUTOS"))
        self.Btn_menu_2.setText(_translate("MainWindow", "DELETAR PRODUTO"))
        self.Btn_menu_3.setText(_translate("MainWindow", "REPOR ESTOQUE"))
        self.Btn_menu_4.setText(_translate("MainWindow", "REMOVER DO ESTOQUE"))
        self.Btn_menu_5.setText(_translate("MainWindow", "VERIFICAR ESTOQUE"))
        self.Btn_menu_6.setText(_translate("MainWindow", "HISTÓRICO DE SAÍDAS"))
        self.Btn_menu_7.setText(_translate("MainWindow", "PROCURAR ITEM"))
        self.Btn_menu_8.setText(_translate("MainWindow", "CONFIGURAÇÕES"))

    def side_menu(self):
        self.frame_left_menu.setMinimumSize(QtCore.QSize(150, 0))

    def new_product(self):
        self.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = newProductWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        print("new product")

    def delete_product(self):
        print("delete product")

    def restock_product(self):
        print("restock product")

    def remove_product(self):
        print("remove product from stock")

    def check_stock(self):
        print("check stock")

    def transaction_history(self):
        print("transaction history")



import file_rc

