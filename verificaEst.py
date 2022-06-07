# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VERIFICARESTOQUE.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verificaEst(object):

    def loadData(self):
        data = sqlite3.connect("inventory.db")
        cur = data.cursor()
        cur.execute("SELECT COUNT() FROM Estoque")
        number = cur.fetchone()
        self.tableWidget.setRowCount(number[0])
        comando = "SELECT * FROM Estoque"
        cur.execute(comando)
        query = cur.fetchall()
        tableIndex = 0
        for row in  query:
            cur.execute("SELECT * FROM Produtos WHERE Cod = :codigo", {'codigo': row[0]})
            produto = cur.fetchone()
            self.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(produto[2])))
            self.tableWidget.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(str(produto[1])))
            tableIndex += 1

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(713, 524)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 0, 601, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(249, 234, 195);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 60, 601, 391))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    border: 3px solid rgb(245, 222, 179);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    background-color:rgb(249, 234, 195);\n"
"    color: rgb(45, 45, 45);\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)

        self.loadData()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "VERIFICAÇÃO DE ESTOQUE"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Cod Prod"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Produto"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Quantidade"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Categoria"))
