# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz6.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Entradas_impresas(object):
    def setupUi(self, Entradas_impresas):
        Entradas_impresas.setObjectName("Entradas_impresas")
        Entradas_impresas.resize(400, 197)
        self.Progreso = QtWidgets.QLabel(Entradas_impresas)
        self.Progreso.setGeometry(QtCore.QRect(120, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Progreso.setFont(font)
        self.Progreso.setObjectName("Progreso")
        self.pushButton = QtWidgets.QPushButton(Entradas_impresas)
        self.pushButton.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Entradas_impresas)
        self.label.setGeometry(QtCore.QRect(120, 50, 151, 81))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Entradas_impresas)
        QtCore.QMetaObject.connectSlotsByName(Entradas_impresas)

    def retranslateUi(self, Entradas_impresas):
        _translate = QtCore.QCoreApplication.translate
        Entradas_impresas.setWindowTitle(_translate("Entradas_impresas", "Entradas impresas"))
        self.Progreso.setText(_translate("Entradas_impresas", "Entradas impresas"))
        self.pushButton.setText(_translate("Entradas_impresas", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Entradas_impresas = QtWidgets.QDialog()
    ui = Ui_Entradas_impresas()
    ui.setupUi(Entradas_impresas)
    Entradas_impresas.show()
    sys.exit(app.exec_())
