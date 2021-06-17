# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from TarifasEntradas import Ui_TarifaEntradas
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog



class Ui_MenuRV(object):

    def ventaEntrada(self):
        self.menu = QDialog()
        self.ui = Ui_TarifaEntradas()
        self.ui.setupUi(self.menu)
        self.menu.show()

    def setupUi(self, MenuRV):
        MenuRV.setObjectName("MenuRV")
        MenuRV.resize(721, 460)
        MenuRV.setMinimumSize(QtCore.QSize(721, 460))
        MenuRV.setMaximumSize(QtCore.QSize(721, 460))
        self.btn_consultar_precio = QtWidgets.QPushButton(MenuRV)
        self.btn_consultar_precio.setGeometry(QtCore.QRect(180, 150, 381, 23))
        self.btn_consultar_precio.setObjectName("btn_consultar_precio")
        self.btn_consultar_venta_entradas = QtWidgets.QPushButton(MenuRV)
        self.btn_consultar_venta_entradas.setGeometry(QtCore.QRect(180, 210, 381, 23))
        self.btn_consultar_venta_entradas.setObjectName("btn_consultar_venta_entradas")
        self.btn_generar_ranking = QtWidgets.QPushButton(MenuRV)
        self.btn_generar_ranking.setGeometry(QtCore.QRect(180, 180, 381, 23))
        self.btn_generar_ranking.setObjectName("btn_generar_ranking")
        self.btn_gestionar_entradas = QtWidgets.QPushButton(MenuRV)
        self.btn_gestionar_entradas.setGeometry(QtCore.QRect(180, 240, 381, 23))
        self.btn_gestionar_entradas.setObjectName("btn_gestionar_entradas")
        self.btn_registrar_venta_entradas = QtWidgets.QPushButton(MenuRV)
        self.btn_registrar_venta_entradas.setGeometry(QtCore.QRect(180, 120, 381, 23))
        self.btn_registrar_venta_entradas.setObjectName("btn_registrar_venta_entradas")
        self.btn_registrar_venta_entradas.clicked.connect(self.ventaEntrada)
        self.btn_registrar_venta_entradas.clicked.connect(MenuRV.close)
        self.lbl_usuario_logueado = QtWidgets.QLabel(MenuRV)
        self.lbl_usuario_logueado.setGeometry(QtCore.QRect(630, 40, 61, 20))
        self.lbl_usuario_logueado.setObjectName("lbl_usuario_logueado")
        self.lbl_nombre_sede = QtWidgets.QLabel(MenuRV)
        self.lbl_nombre_sede.setGeometry(QtCore.QRect(630, 10, 71, 16))
        self.lbl_nombre_sede.setObjectName("lbl_nombre_sede")
        self.lbl_fecha = QtWidgets.QLabel(MenuRV)
        self.lbl_fecha.setGeometry(QtCore.QRect(630, 70, 91, 20))
        self.lbl_fecha.setObjectName("lbl_fecha")
        self.btn_cerrar_sesion = QtWidgets.QPushButton(MenuRV)
        self.btn_cerrar_sesion.setGeometry(QtCore.QRect(180, 290, 381, 23))
        self.btn_cerrar_sesion.setObjectName("btn_cerrar_sesion")
        self.line = QtWidgets.QFrame(MenuRV)
        self.line.setGeometry(QtCore.QRect(180, 270, 381, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(MenuRV)
        self.btn_cerrar_sesion.clicked.connect(MenuRV.reject)
        QtCore.QMetaObject.connectSlotsByName(MenuRV)

    def retranslateUi(self, MenuRV):
        _translate = QtCore.QCoreApplication.translate
        MenuRV.setWindowTitle(_translate("MenuRV", "Menu principal"))
        self.btn_consultar_precio.setText(_translate("MenuRV", "Consultar precio de entradas"))
        self.btn_consultar_venta_entradas.setText(_translate("MenuRV", "Consultar venta de entrada"))
        self.btn_generar_ranking.setText(_translate("MenuRV", "Generar Ranking de venta de entradas"))
        self.btn_gestionar_entradas.setText(_translate("MenuRV", "Gestionar entradas"))
        self.btn_registrar_venta_entradas.setText(_translate("MenuRV", "Registrar venta de entradas"))
        self.lbl_usuario_logueado.setText(_translate("MenuRV", "Usuario"))
        self.lbl_nombre_sede.setText(_translate("MenuRV", "Nombre sede"))
        self.lbl_fecha.setText(_translate("MenuRV", "Fecha y hora"))
        self.btn_cerrar_sesion.setText(_translate("MenuRV", "Cerrar sesión"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuRV = QtWidgets.QDialog()
    ui = Ui_MenuRV()
    ui.setupUi(MenuRV)
    MenuRV.show()
    sys.exit(app.exec_())
