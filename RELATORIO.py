# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RELATORIO.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3


class Ui_Form(object):

    @staticmethod
    def mm2p(milimetros):
        return milimetros / 0.352777

    def gerearpdf(self):
        data = sqlite3.connect("inventory.db")
        cur = data.cursor()
        cnv = canvas.Canvas("meu_pdf.pdf")
        input = (self.lineEdit.text()).split('/')
        mes = input[0]
        ano = input[1]




        cnv.drawString(self.mm2p(22),self.mm2p(275), "ID")
        cnv.drawString(self.mm2p(42), self.mm2p(275), "TIPO")
        cnv.drawString(self.mm2p(72), self.mm2p(275), "PRODUTO")
        cnv.drawString(self.mm2p(104), self.mm2p(275), "QUANTIDADE")
        cnv.drawString(self.mm2p(140), self.mm2p(275), "DATA")

        eixoy = 250
        # select * from Movimentacao where strftime('%m', Data) = '06' and  strftime('%Y', Data) = '2022';
        # cur.execute("SELECT * FROM Login WHERE UserID = :login AND Password = :passwd",{'login': self.lineEdit_user.text(), 'passwd': pwd})
        cur.execute("select * from Movimentacao where strftime('%m', Data) = :month and  strftime('%Y', Data) = :year;",
                    {'month': mes, 'year': ano})
        results = cur.fetchall()
        for row in results:
            cnv.drawString(self.mm2p(22), self.mm2p(eixoy), str(row[0]))
            cnv.drawString(self.mm2p(42), self.mm2p(eixoy), str(row[1]))
            cnv.drawString(self.mm2p(72), self.mm2p(eixoy), str(row[2]))
            cnv.drawString(self.mm2p(104), self.mm2p(eixoy), str(row[3]))
            cnv.drawString(self.mm2p(140), self.mm2p(eixoy), str(row[4]))

            eixoy -= 15
        data.close()
        cnv.save()

    def loadData(self):
        data = sqlite3.connect("inventory.db")
        cur = data.cursor()
        cur.execute("SELECT COUNT() FROM Movimentacao")
        number = cur.fetchone()
        self.tableWidget.setRowCount(number[0])
        cur.execute("SELECT * FROM Movimentacao")
        results = cur.fetchall()
        tableIndex = 0
        for row in results:
            cur.execute("SELECT * FROM Produtos WHERE Cod = :codigo", {'codigo': row[2]})
            produto = cur.fetchone()
            self.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(produto[2])))
            self.tableWidget.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tableIndex, 4, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tableIndex, 5, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tableIndex, 6, QtWidgets.QTableWidgetItem(str(produto[3])))
            tableIndex += 1

    def attData(self):
            input = (self.lineEdit.text()).split('/')
            mes = input[0]
            ano = input[1]
            data = sqlite3.connect("inventory.db")
            cur = data.cursor()
            cur.execute("SELECT COUNT() FROM Movimentacao where strftime('%m', Data) = :month and  strftime('%Y', Data) = :year;", {'month': mes, 'year': ano})
            number = cur.fetchone()
            self.tableWidget.setRowCount(number[0])
            cur.execute("SELECT * FROM Movimentacao where strftime('%m', Data) = :month and  strftime('%Y', Data) = :year;", {'month': mes, 'year': ano})
            results = cur.fetchall()
            tableIndex = 0
            for row in results:
                cur.execute("SELECT * FROM Produtos WHERE Cod = :codigo", {'codigo': row[2]})
                produto = cur.fetchone()
                self.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(produto[2])))
                self.tableWidget.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tableWidget.setItem(tableIndex, 4, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(tableIndex, 5, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tableWidget.setItem(tableIndex, 6, QtWidgets.QTableWidgetItem(str(produto[3])))
                tableIndex += 1

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(828, 868)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(80, 160, 641, 201))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    border: 3px solid rgb(245, 222, 179);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    background-color:rgb(249, 234, 195);\n"
"    color: rgb(45, 45, 45);\n"
"}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 641, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color:rgb(249, 234, 195);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 90, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 3px solid rgb(245, 222, 179);\n"
"    border-radius: 10px;\n"
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
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(520, 90, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{    \n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 380, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{    \n"
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
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Cod. Prod"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Categoria"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Valor"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Custo"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Fornecedor"))
        self.pushButton.clicked.connect(lambda : self.attData())
        self.pushButton_2.clicked.connect(lambda : self.gerearpdf())
        self.label.setText(_translate("Form", "RELATÓRIO MENSAL"))
        self.lineEdit.setPlaceholderText(_translate("Form", "DATA"))
        self.pushButton.setText(_translate("Form", "ATUALIZAR"))
        self.pushButton_2.setText(_translate("Form", "GERAR RELATÓRIO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
