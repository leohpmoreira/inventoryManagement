# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadProd.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator


class Ui_cadProd(object):

    def cadastra(self):
        data = sqlite3.connect("inventory.db")
        cur = data.cursor()
        nome = self.nome.text()
        categoria = self.categoria.text()
        valor = float(self.valor.text())
        custo = float(self.custo.text())
        fabricante = self.fornecedor.text()
        codigo = self.codigo.text()

        if nome and categoria and valor and fabricante and codigo:
             cur.execute("SELECT * FROM Categoria WHERE Nome = :nome",{'nome': categoria})
             cod_cat = cur.fetchone()
             try:
                 cur.execute("INSERT INTO Produtos VALUES (:cod_prod,:cod_cat,:nome,:fabricante,:custo,:preco)",\
                   {'cod_prod': codigo, 'cod_cat':cod_cat[0], 'nome': nome, 'fabricante': fabricante, 'custo': custo, 'preco': valor})
                 data.commit()
                 cur.close()
                 data.close()
                 self.codigo.clear()
                 self.fornecedor.clear()
                 self.nome.clear()
                 self.categoria.clear()
                 self.custo.clear()
                 self.valor.clear()
             except:
                 print("Nao e possivel inserir")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 400)
        self.custo = QtWidgets.QLineEdit(Form)
        self.custo.setGeometry(QtCore.QRect(520, 70, 151, 41))
        self.custo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.custo.setText("")
        self.custo.setObjectName("custo")
        self.nome = QtWidgets.QLineEdit(Form)
        self.nome.setGeometry(QtCore.QRect(150, 70, 151, 41))
        self.nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome.setText("")
        self.nome.setObjectName("nome")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 211, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.valor = QtWidgets.QLineEdit(Form)
        self.valor.setGeometry(QtCore.QRect(330, 120, 151, 41))
        self.valor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valor.setText("")
        self.valor.setObjectName("valor")
        self.fornecedor = QtWidgets.QLineEdit(Form)
        self.fornecedor.setGeometry(QtCore.QRect(520, 120, 151, 41))
        self.fornecedor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fornecedor.setText("")
        self.fornecedor.setObjectName("fornecedor")
        self.categoria = QtWidgets.QLineEdit(Form)
        self.categoria.setGeometry(QtCore.QRect(150, 120, 151, 41))
        self.categoria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.categoria.setText("")
        self.categoria.setObjectName("categoria")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 220, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.codigo = QtWidgets.QLineEdit(Form)
        self.codigo.setGeometry(QtCore.QRect(330, 70, 151, 41))
        self.codigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.codigo.setText("")
        self.codigo.setObjectName("codigo")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(150, 170, 151, 31))
        self.comboBox.setObjectName("comboBox")

        self.onlyfloat = QDoubleValidator()

        self.custo.setValidator(self.onlyfloat)
        self.valor.setValidator(self.onlyfloat)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.custo.setPlaceholderText(_translate("Form", "Custo"))
        self.nome.setPlaceholderText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "CADASTRAR PRODUTO"))
        self.valor.setPlaceholderText(_translate("Form", "Valor"))
        self.fornecedor.setPlaceholderText(_translate("Form", "Fornecedor"))
        self.categoria.setPlaceholderText(_translate("Form", "Categoria"))
        self.pushButton_2.setText(_translate("Form", "CADASTRAR"))
        self.codigo.setPlaceholderText(_translate("Form", "Código"))