# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 162)
        Dialog.setMinimumSize(QtCore.QSize(400, 162))
        Dialog.setMaximumSize(QtCore.QSize(400, 162))
        self.Progreso = QtWidgets.QLabel(Dialog)
        self.Progreso.setGeometry(QtCore.QRect(110, 40, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Progreso.setFont(font)
        self.Progreso.setObjectName("Progreso")
        self.PB_imprimir_entradas = QtWidgets.QProgressBar(Dialog)
        self.PB_imprimir_entradas.setGeometry(QtCore.QRect(120, 90, 181, 23))
        self.PB_imprimir_entradas.setProperty("value", 24)
        self.PB_imprimir_entradas.setObjectName("PB_imprimir_entradas")

        self.retranslateUi(Dialog)
        self.PB_imprimir_entradas.valueChanged['int'].connect(self.PB_imprimir_entradas.setMaximum)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Progreso.setText(_translate("Dialog", "Imprimiendo entradas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())