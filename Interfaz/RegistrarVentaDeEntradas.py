# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 300)
        self.ComboBox = QtWidgets.QComboBox(Dialog)
        self.ComboBox.setGeometry(QtCore.QRect(40, 50, 151, 22))
        self.ComboBox.setObjectName("ComboBox")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 141, 16))
        self.label_2.setObjectName("label_2")
        self.ComboBox_2 = QtWidgets.QComboBox(Dialog)
        self.ComboBox_2.setGeometry(QtCore.QRect(40, 110, 151, 22))
        self.ComboBox_2.setObjectName("ComboBox_2")
        self.ComboBox_2.addItem("")
        self.ComboBox_2.addItem("")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(40, 150, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 150, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QtCore.QRect(300, 30, 531, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
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
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(40, 200, 151, 22))
        self.spinBox.setMaximum(1000)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 51, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 240, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 240, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ComboBox.setItemText(0, _translate("Dialog", "General"))
        self.ComboBox.setItemText(1, _translate("Dialog", "Menores"))
        self.ComboBox.setItemText(2, _translate("Dialog", "Jubilados"))
        self.ComboBox.setItemText(3, _translate("Dialog", "Estudiantes"))
        self.ComboBox.setItemText(4, _translate("Dialog", "Otra"))
        self.label.setText(_translate("Dialog", "Seleccionar tipo de entrada:"))
        self.label_2.setText(_translate("Dialog", "Seleccionar tipo de visita:"))
        self.ComboBox_2.setItemText(0, _translate("Dialog", "Completa"))
        self.ComboBox_2.setItemText(1, _translate("Dialog", "Por exposicion"))
        self.radioButton.setText(_translate("Dialog", "Con guía"))
        self.radioButton_2.setText(_translate("Dialog", "Sin guía"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Tipo entrada"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tipo visita"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Guia"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Cantidad"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Precio"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "General"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "Completa"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "no"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Dialog", "123"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("Dialog", "Cantidad:"))
        self.pushButton.setText(_translate("Dialog", "Agregar"))
        self.pushButton_2.setText(_translate("Dialog", "Confirmar"))
        self.pushButton_3.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())