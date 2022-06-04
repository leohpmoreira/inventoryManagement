# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menuzin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from CadProd import Ui_cadProd
from configuracoes import Ui_config
from deletarproduto import Ui_deleta
from historico import Ui_historico
from procura import Ui_procura
from remocao import Ui_remocao
from reposicao import Ui_reposicao
from verificaEst import Ui_verificaEst


class menu_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
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
        self.Btn_toggle = QtWidgets.QPushButton(self.frame_top)
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
        self.frame_left_menu.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.Btn_cadProd = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_cadProd.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_cadProd.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_cadProd.setObjectName("Btn_cadProd")
        self.verticalLayout_4.addWidget(self.Btn_cadProd)
        self.Btn_delProd = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_delProd.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_delProd.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_delProd.setObjectName("Btn_delProd")
        self.verticalLayout_4.addWidget(self.Btn_delProd)
        self.Btn_reoEst = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_reoEst.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_reoEst.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_reoEst.setObjectName("Btn_reoEst")
        self.verticalLayout_4.addWidget(self.Btn_reoEst)
        self.Btn_remEst = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_remEst.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_remEst.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_remEst.setObjectName("Btn_remEst")
        self.verticalLayout_4.addWidget(self.Btn_remEst)
        self.Btn_verEst = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_verEst.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_verEst.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_verEst.setObjectName("Btn_verEst")
        self.verticalLayout_4.addWidget(self.Btn_verEst)
        self.Btn_hisSai = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_hisSai.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_hisSai.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_hisSai.setObjectName("Btn_hisSai")
        self.verticalLayout_4.addWidget(self.Btn_hisSai)
        self.Btn_procItem = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_procItem.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_procItem.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_procItem.setObjectName("Btn_procItem")
        self.verticalLayout_4.addWidget(self.Btn_procItem)
        self.Btn_config = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_config.setMinimumSize(QtCore.QSize(0, 50))
        self.Btn_config.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_config.setObjectName("Btn_config")
        self.verticalLayout_4.addWidget(self.Btn_config)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PagesWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.PagesWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.PagesWidget.setMaximumSize(QtCore.QSize(900, 16777215))
        self.PagesWidget.setObjectName("PagesWidget")
        self.reg_prod = QtWidgets.QWidget()
        self.reg_prod.setObjectName("reg_prod")
        self.PagesWidget.addWidget(self.reg_prod)
        self.deleta_prod = QtWidgets.QWidget()
        self.deleta_prod.setObjectName("deleta_prod")
        self.PagesWidget.addWidget(self.deleta_prod)
        self.repor_est = QtWidgets.QWidget()
        self.repor_est.setObjectName("repor_est")
        self.PagesWidget.addWidget(self.repor_est)
        self.remover_est = QtWidgets.QWidget()
        self.remover_est.setObjectName("remover_est")
        self.PagesWidget.addWidget(self.remover_est)
        self.verificar_est = QtWidgets.QWidget()
        self.verificar_est.setObjectName("verificar_est")
        self.PagesWidget.addWidget(self.verificar_est)
        self.hist_saida = QtWidgets.QWidget()
        self.hist_saida.setObjectName("hist_saida")
        self.PagesWidget.addWidget(self.hist_saida)
        self.procura_item = QtWidgets.QWidget()
        self.procura_item.setObjectName("procura_item")
        self.PagesWidget.addWidget(self.procura_item)
        self.config = QtWidgets.QWidget()
        self.config.setObjectName("config")
        self.PagesWidget.addWidget(self.config)
        self.verticalLayout_5.addWidget(self.PagesWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        cadProd = Ui_cadProd()
        cadProd.setupUi(self.reg_prod)
        self.reg_prod.show()

        config = Ui_config()
        config.setupUi(self.config)
        self.config.show()

        deleta = Ui_deleta()
        deleta.setupUi(self.deleta_prod)
        self.deleta_prod.show()

        hist = Ui_historico()
        hist.setupUi(self.hist_saida)
        self.hist_saida.show()

        procura = Ui_procura()
        procura.setupUi(self.procura_item)
        self.procura_item.show()

        remocao = Ui_remocao()
        remocao.setupUi(self.remover_est)
        self.remover_est.show()

        reposicao = Ui_reposicao()
        reposicao.setupUi(self.repor_est)
        self.remover_est.show()

        verficarEst = Ui_verificaEst()
        verficarEst.setupUi(self.verificar_est)
        self.verificar_est.show()


        self.Btn_cadProd.clicked.connect(lambda : self.PagesWidget.setCurrentWidget(self.reg_prod))
        self.Btn_remEst.clicked.connect(lambda: self.PagesWidget.setCurrentWidget(self.remover_est))
        self.Btn_reoEst.clicked.connect(lambda: self.PagesWidget.setCurrentWidget(self.repor_est))
        self.Btn_delProd.clicked.connect(lambda: self.PagesWidget.setCurrentWidget(self.deleta_prod))
        self.Btn_procItem.clicked.connect(lambda: self.PagesWidget.setCurrentWidget(self.procura_item))
        self.Btn_config.clicked.connect(lambda: self.PagesWidget.setCurrentWidget(self.config))
        self.Btn_verEst.clicked.connect(lambda: self.PagesWidget.setCurrentWidget(self.verificar_est))
        self.Btn_hisSai.clicked.connect(lambda: self.PagesWidget.setCurrentWidget(self.hist_saida))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_toggle.setText(_translate("MainWindow", "TOGGLE"))
        self.Btn_cadProd.setText(_translate("MainWindow", "CADASTRAR PRODUTOS"))
        self.Btn_delProd.setText(_translate("MainWindow", "DELETAR PRODUTO"))
        self.Btn_reoEst.setText(_translate("MainWindow", "REPOR ESTOQUE"))
        self.Btn_remEst.setText(_translate("MainWindow", "REMOVER DO ESTOQUE"))
        self.Btn_verEst.setText(_translate("MainWindow", "VERIFICAR ESTOQUE"))
        self.Btn_hisSai.setText(_translate("MainWindow", "HISTÓRICO DE SAÍDAS"))
        self.Btn_procItem.setText(_translate("MainWindow", "PROCURAR ITEM"))
        self.Btn_config.setText(_translate("MainWindow", "CONFIGURAÇÕES"))
import file_rc
