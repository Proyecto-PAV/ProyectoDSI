# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\felip\Desktop\ProyectoDSI\Interfaz\Interfaz3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistrarVentaDeEntradas(object):
    def setupUi(self, RegistrarVentaDeEntradas):
        RegistrarVentaDeEntradas.setObjectName("RegistrarVentaDeEntradas")
        RegistrarVentaDeEntradas.setEnabled(True)
        RegistrarVentaDeEntradas.resize(1050, 310)
        RegistrarVentaDeEntradas.setMinimumSize(QtCore.QSize(1050, 310))
        RegistrarVentaDeEntradas.setMaximumSize(QtCore.QSize(1050, 310))
        self.CB_tipo_entrada = QtWidgets.QComboBox(RegistrarVentaDeEntradas)
        self.CB_tipo_entrada.setGeometry(QtCore.QRect(40, 50, 151, 22))
        self.CB_tipo_entrada.setObjectName("CB_tipo_entrada")
        self.CB_tipo_entrada.addItem("")
        self.CB_tipo_entrada.addItem("")
        self.CB_tipo_entrada.addItem("")
        self.CB_tipo_entrada.addItem("")
        self.CB_tipo_entrada.addItem("")
        self.lbl_tipo_entrada = QtWidgets.QLabel(RegistrarVentaDeEntradas)
        self.lbl_tipo_entrada.setGeometry(QtCore.QRect(40, 30, 141, 16))
        self.lbl_tipo_entrada.setObjectName("lbl_tipo_entrada")
        self.lbl_tipo_visita = QtWidgets.QLabel(RegistrarVentaDeEntradas)
        self.lbl_tipo_visita.setGeometry(QtCore.QRect(40, 90, 141, 16))
        self.lbl_tipo_visita.setObjectName("lbl_tipo_visita")
        self.CB_tipo_visita = QtWidgets.QComboBox(RegistrarVentaDeEntradas)
        self.CB_tipo_visita.setGeometry(QtCore.QRect(40, 110, 151, 22))
        self.CB_tipo_visita.setObjectName("CB_tipo_visita")
        self.CB_tipo_visita.addItem("")
        self.CB_tipo_visita.addItem("")
        self.RB_con_guia = QtWidgets.QRadioButton(RegistrarVentaDeEntradas)
        self.RB_con_guia.setGeometry(QtCore.QRect(40, 150, 82, 17))
        self.RB_con_guia.setObjectName("RB_con_guia")
        self.RB_sin_guia = QtWidgets.QRadioButton(RegistrarVentaDeEntradas)
        self.RB_sin_guia.setGeometry(QtCore.QRect(130, 150, 82, 17))
        self.RB_sin_guia.setObjectName("RB_sin_guia")
        self.tableWidget = QtWidgets.QTableWidget(RegistrarVentaDeEntradas)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(340, 30, 681, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        self.tableWidget.setVerticalHeaderItem(0, item)
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
        self.SB_cantidad = QtWidgets.QSpinBox(RegistrarVentaDeEntradas)
        self.SB_cantidad.setGeometry(QtCore.QRect(40, 200, 151, 22))
        self.SB_cantidad.setMaximum(1000)
        self.SB_cantidad.setObjectName("SB_cantidad")
        self.lbl_cantidad = QtWidgets.QLabel(RegistrarVentaDeEntradas)
        self.lbl_cantidad.setGeometry(QtCore.QRect(40, 180, 51, 16))
        self.lbl_cantidad.setObjectName("lbl_cantidad")
        self.btn_agregar = QtWidgets.QPushButton(RegistrarVentaDeEntradas)
        self.btn_agregar.setGeometry(QtCore.QRect(80, 240, 71, 23))
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_confirmar = QtWidgets.QPushButton(RegistrarVentaDeEntradas)
        self.btn_confirmar.setGeometry(QtCore.QRect(620, 260, 75, 23))
        self.btn_confirmar.setObjectName("btn_confirmar")
        self.btn_cancelar = QtWidgets.QPushButton(RegistrarVentaDeEntradas)
        self.btn_cancelar.setGeometry(QtCore.QRect(710, 260, 75, 23))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.lbl_precio_tipo_entrada = QtWidgets.QLabel(RegistrarVentaDeEntradas)
        self.lbl_precio_tipo_entrada.setGeometry(QtCore.QRect(240, 50, 91, 16))
        self.lbl_precio_tipo_entrada.setObjectName("lbl_precio_tipo_entrada")
        self.lbl_precio_tipo_visita = QtWidgets.QLabel(RegistrarVentaDeEntradas)
        self.lbl_precio_tipo_visita.setGeometry(QtCore.QRect(240, 110, 91, 16))
        self.lbl_precio_tipo_visita.setObjectName("lbl_precio_tipo_visita")
        self.lbl_adicional_guia = QtWidgets.QLabel(RegistrarVentaDeEntradas)
        self.lbl_adicional_guia.setGeometry(QtCore.QRect(240, 150, 91, 16))
        self.lbl_adicional_guia.setObjectName("lbl_adicional_guia")
        self.line = QtWidgets.QFrame(RegistrarVentaDeEntradas)
        self.line.setGeometry(QtCore.QRect(210, 40, 16, 141))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(RegistrarVentaDeEntradas)
        self.btn_cancelar.clicked.connect(RegistrarVentaDeEntradas.reject)
        QtCore.QMetaObject.connectSlotsByName(RegistrarVentaDeEntradas)

    def retranslateUi(self, RegistrarVentaDeEntradas):
        _translate = QtCore.QCoreApplication.translate
        RegistrarVentaDeEntradas.setWindowTitle(_translate("RegistrarVentaDeEntradas", "Registrar venta de entradas"))
        self.CB_tipo_entrada.setItemText(0, _translate("RegistrarVentaDeEntradas", "General"))
        self.CB_tipo_entrada.setItemText(1, _translate("RegistrarVentaDeEntradas", "Menores"))
        self.CB_tipo_entrada.setItemText(2, _translate("RegistrarVentaDeEntradas", "Jubilados"))
        self.CB_tipo_entrada.setItemText(3, _translate("RegistrarVentaDeEntradas", "Estudiantes"))
        self.CB_tipo_entrada.setItemText(4, _translate("RegistrarVentaDeEntradas", "Otra"))
        self.lbl_tipo_entrada.setText(_translate("RegistrarVentaDeEntradas", "Seleccionar tipo de entrada:"))
        self.lbl_tipo_visita.setText(_translate("RegistrarVentaDeEntradas", "Seleccionar tipo de visita:"))
        self.CB_tipo_visita.setItemText(0, _translate("RegistrarVentaDeEntradas", "Completa"))
        self.CB_tipo_visita.setItemText(1, _translate("RegistrarVentaDeEntradas", "Por exposicion"))
        self.RB_con_guia.setText(_translate("RegistrarVentaDeEntradas", "Con guía"))
        self.RB_sin_guia.setText(_translate("RegistrarVentaDeEntradas", "Sin guía"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("RegistrarVentaDeEntradas", "Total"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RegistrarVentaDeEntradas", "Tipo entrada"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RegistrarVentaDeEntradas", "Tipo visita"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RegistrarVentaDeEntradas", "Guia"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RegistrarVentaDeEntradas", "Cantidad"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("RegistrarVentaDeEntradas", "Precio"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("RegistrarVentaDeEntradas", "Eliminar"))
        self.lbl_cantidad.setText(_translate("RegistrarVentaDeEntradas", "Cantidad:"))
        self.btn_agregar.setText(_translate("RegistrarVentaDeEntradas", "Agregar"))
        self.btn_confirmar.setText(_translate("RegistrarVentaDeEntradas", "Confirmar"))
        self.btn_cancelar.setText(_translate("RegistrarVentaDeEntradas", "Cancelar"))
        self.lbl_precio_tipo_entrada.setText(_translate("RegistrarVentaDeEntradas", "Precio: $"))
        self.lbl_precio_tipo_visita.setText(_translate("RegistrarVentaDeEntradas", "Precio: $"))
        self.lbl_adicional_guia.setText(_translate("RegistrarVentaDeEntradas", "Adicional: $"))
