# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
sys.path.append('../')
from Pantalla import PantallaVentaEntradas
from VentaEntradas import Ui_RegistrarVentaDeEntradas
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QAbstractItemView, QDialog
from BaseDeDatos.CapaConexion import *


class Ui_TarifaEntradas(object):

    def __init__(pantallaVentaEntradas):
        pantallaVentaEntradas = pantallaVentaEntradas

    def obtenerTarifas(self):
        self.pantallaVentaEntradas = PantallaVentaEntradas(None, None, None, None, None, None, None, None, None, None )
        tarifasVigentes, montoAdicionalGuia = self.pantallaVentaEntradas.tomarOpcionRegistrarVentaEntradas()
        self.lbl_adicional_guia.setText("$" + str(montoAdicionalGuia))
        for tarifa in tarifasVigentes:
            tipo_entrada = tarifa.tipo_entrada
            tipo_visita = tarifa.tipo_visita
            monto = tarifa.monto
            rowPosition = self.t_tarifas.rowCount()
            self.t_tarifas.insertRow(rowPosition)
            self.t_tarifas.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(tipo_entrada))
            self.t_tarifas.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(tipo_visita))
            self.t_tarifas.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(monto)))
            borrarDetalles()

    
    def seleccionTarifa(self):
        row = self.t_tarifas.currentRow()
        tipo_entrada = (self.t_tarifas.item(row, 0).text())
        tipo_visita = (self.t_tarifas.item(row, 1).text())
        monto = (self.t_tarifas.item(row, 2).text())
        if self.RB_con_guia.isChecked():
            tarifasVigentes, adicionalPorGuia = self.pantallaVentaEntradas.tomarOpcionRegistrarVentaEntradas()
            montoTotal = float(monto) + adicionalPorGuia
            if self.SP_cantidad.isHidden():
                self.pantallaVentaEntradas.tomarDatosEntrada(tipo_visita, tipo_entrada, True)
                self.SP_cantidad.show()
            else:
                valor_spin = self.SP_cantidad.value()
                if valor_spin > 0:
                    validacion = self.pantallaVentaEntradas.tomarSeleccionDeCantidadEntradasEmitir(valor_spin)
                    if validacion:
                        total = valor_spin * montoTotal
                        insertarEntrada(tipo_entrada, tipo_visita, montoTotal, valor_spin, total, True)
                        self.vtaEntradas = QDialog()
                        self.ui = Ui_RegistrarVentaDeEntradas(self.pantallaVentaEntradas)
                        self.ui.setupUi(self.vtaEntradas)
                        self.ui.pantallaVentaEntradas = self.pantallaVentaEntradas
                        self.vtaEntradas.show()

        elif self.RB_sin_guia.isChecked():
            if self.SP_cantidad.isHidden():
                self.pantallaVentaEntradas.tomarDatosEntrada(tipo_visita, tipo_entrada, False)
                self.SP_cantidad.show()
            else:
                valor_spin = self.SP_cantidad.value()
                if valor_spin > 0:
                    validacion = self.pantallaVentaEntradas.tomarSeleccionDeCantidadEntradasEmitir(valor_spin)
                    if validacion:
                        total = valor_spin * float(monto)
                        insertarEntrada(tipo_entrada, tipo_visita, monto, valor_spin, total, False)
                        self.vtaEntradas = QDialog()
                        self.ui = Ui_RegistrarVentaDeEntradas(self.pantallaVentaEntradas)
                        self.ui.setupUi(self.vtaEntradas)
                        self.ui.pantallaVentaEntradas = self.pantallaVentaEntradas
                        self.vtaEntradas.show()
                else:
                    pass
        


    def setupUi(self, TarifaEntradas):
        TarifaEntradas.setObjectName("TarifaEntradas")
        TarifaEntradas.resize(750, 400)
        TarifaEntradas.setMinimumSize(QtCore.QSize(750, 400))
        TarifaEntradas.setMaximumSize(QtCore.QSize(750, 400))
        #*-------------------------Tabla---------------------------------------
        self.t_tarifas = QtWidgets.QTableWidget(TarifaEntradas)
        self.t_tarifas.setGeometry(QtCore.QRect(50, 40, 321, 291))
        self.t_tarifas.setObjectName("t_tarifas")
        self.t_tarifas.setColumnCount(3)
        self.t_tarifas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.t_tarifas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.t_tarifas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.t_tarifas.setHorizontalHeaderItem(2, item)
        self.t_tarifas.setSelectionBehavior(QAbstractItemView.SelectRows)
        #*--------------------------------------------------------------------
        self.line = QtWidgets.QFrame(TarifaEntradas)
        self.line.setGeometry(QtCore.QRect(510, 40, 161, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(TarifaEntradas)
        self.label.setGeometry(QtCore.QRect(580, 30, 47, 13))
        self.label.setObjectName("label")
        #*---------------------------------------------------------------
        self.RB_con_guia = QtWidgets.QRadioButton(TarifaEntradas)
        self.RB_con_guia.setGeometry(QtCore.QRect(520, 60, 82, 17))
        self.RB_con_guia.setObjectName("RB_con_guia")
        self.RB_sin_guia = QtWidgets.QRadioButton(TarifaEntradas)
        self.RB_sin_guia.setGeometry(QtCore.QRect(610, 60, 82, 17))
        self.RB_sin_guia.setObjectName("RB_sin_guia")
        #*---------------------------------------------------------------
        self.line_2 = QtWidgets.QFrame(TarifaEntradas)
        self.line_2.setGeometry(QtCore.QRect(510, 120, 161, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(TarifaEntradas)
        self.label_2.setGeometry(QtCore.QRect(550, 110, 91, 16))
        self.label_2.setObjectName("label_2")
        self.lbl_adicional_guia = QtWidgets.QLabel(TarifaEntradas)
        self.lbl_adicional_guia.setGeometry(QtCore.QRect(580, 140, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_adicional_guia.setFont(font)
        self.lbl_adicional_guia.setText("")
        self.lbl_adicional_guia.setObjectName("lbl_adicional_guia")
        self.line_3 = QtWidgets.QFrame(TarifaEntradas)
        self.line_3.setGeometry(QtCore.QRect(510, 190, 161, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(TarifaEntradas)
        self.label_4.setGeometry(QtCore.QRect(570, 180, 47, 13))
        self.label_4.setObjectName("label_4")
        self.SP_cantidad = QtWidgets.QSpinBox(TarifaEntradas)
        self.SP_cantidad.setGeometry(QtCore.QRect(510, 220, 161, 22))
        self.SP_cantidad.setObjectName("SP_cantidad")
        self.SP_cantidad.setMaximum(999)
        self.SP_cantidad.hide()
        self.btn_confirmar_seleccion_tarifa = QtWidgets.QPushButton(TarifaEntradas)
        self.btn_confirmar_seleccion_tarifa.setGeometry(QtCore.QRect(510, 270, 75, 23))
        self.btn_confirmar_seleccion_tarifa.setObjectName("btn_confirmar_seleccion_tarifa")
        self.btn_cancelar_seleccion_tarifa = QtWidgets.QPushButton(TarifaEntradas)
        self.btn_cancelar_seleccion_tarifa.setGeometry(QtCore.QRect(600, 270, 75, 23))
        self.btn_cancelar_seleccion_tarifa.setObjectName("btn_cancelar_seleccion_tarifa")
        self.lbl_error = QtWidgets.QLabel(TarifaEntradas)
        self.lbl_error.setGeometry(QtCore.QRect(450, 310, 301, 20))
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")
        self.label_3 = QtWidgets.QLabel(TarifaEntradas)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 47, 13))
        self.label_3.setObjectName("label_3")
        self.btn_buscar_tarifas = QtWidgets.QPushButton(TarifaEntradas)
        self.btn_buscar_tarifas.setGeometry(QtCore.QRect(170, 350, 81, 23))
        self.btn_buscar_tarifas.setObjectName("btn_buscar_tarifas")
        self.btn_buscar_tarifas.clicked.connect(self.obtenerTarifas)
        self.btn_confirmar_seleccion_tarifa.clicked.connect(self.seleccionTarifa)
        #self.btn_confirmar_seleccion_tarifa.clicked.connect(self.seleccionTarifa)
        self.retranslateUi(TarifaEntradas)
        QtCore.QMetaObject.connectSlotsByName(TarifaEntradas)

    def retranslateUi(self, TarifaEntradas):
        _translate = QtCore.QCoreApplication.translate
        TarifaEntradas.setWindowTitle(_translate("TarifaEntradas", "Dialog"))
        item = self.t_tarifas.horizontalHeaderItem(0)
        item.setText(_translate("TarifaEntradas", "Tipo entrada"))
        item = self.t_tarifas.horizontalHeaderItem(1)
        item.setText(_translate("TarifaEntradas", "Tipo visita"))
        item = self.t_tarifas.horizontalHeaderItem(2)
        item.setText(_translate("TarifaEntradas", "Monto"))
        self.label.setText(_translate("TarifaEntradas", "Guía"))
        self.RB_con_guia.setText(_translate("TarifaEntradas", "Con guía"))
        self.RB_sin_guia.setText(_translate("TarifaEntradas", "Sin guía"))
        self.label_2.setText(_translate("TarifaEntradas", "Adicional por guía"))
        self.label_4.setText(_translate("TarifaEntradas", "Cantidad"))
        self.btn_confirmar_seleccion_tarifa.setText(_translate("TarifaEntradas", "Confirmar"))
        self.btn_cancelar_seleccion_tarifa.setText(_translate("TarifaEntradas", "Cancelar"))
        self.label_3.setText(_translate("TarifaEntradas", "Tarifas"))
        self.btn_buscar_tarifas.setText(_translate("TarifaEntradas", "Buscar tarifas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TarifaEntradas = QtWidgets.QDialog()
    ui = Ui_TarifaEntradas()
    ui.setupUi(TarifaEntradas)
    TarifaEntradas.show()
    sys.exit(app.exec_())
