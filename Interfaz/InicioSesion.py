# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from Menu import Ui_MenuRV
from Pantalla import usuario
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QWidget
from PyQt5 import uic


class Ui_InicioSesion(QMainWindow):
    def menu(self, event):
        res = usuario(self.LE_usuario.text(), self.LE_contra.text())
        if res == True:
            self.menu = QDialog()
            self.ui = Ui_MenuRV()
            self.ui.setupUi(self.menu)
            self.menu.show()
        else:
            pass
                
            

    def setupUi(self, InicioSesion):
        InicioSesion.setObjectName("InicioSesion")
        InicioSesion.setEnabled(True)
        InicioSesion.resize(640, 480)
        InicioSesion.setMinimumSize(QtCore.QSize(640, 480))
        InicioSesion.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        InicioSesion.setFont(font)
        InicioSesion.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(InicioSesion)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_iniciar_sesion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iniciar_sesion.setGeometry(QtCore.QRect(280, 280, 81, 23))
        self.btn_iniciar_sesion.clicked.connect(self.menu)
        self.btn_iniciar_sesion.clicked.connect(InicioSesion.close)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_iniciar_sesion.setFont(font)
        self.btn_iniciar_sesion.setObjectName("btn_iniciar_sesion")
        self.lbl_usuario = QtWidgets.QLabel(self.centralwidget)
        self.lbl_usuario.setGeometry(QtCore.QRect(170, 210, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.lbl_contra = QtWidgets.QLabel(self.centralwidget)
        self.lbl_contra.setGeometry(QtCore.QRect(170, 240, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lbl_contra.setFont(font)
        self.lbl_contra.setObjectName("lbl_contra")
        self.LE_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_usuario.setGeometry(QtCore.QRect(240, 210, 161, 20))
        self.LE_usuario.setText("")
        self.LE_usuario.setObjectName("LE_usuario")
        self.LE_contra = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_contra.setGeometry(QtCore.QRect(240, 240, 161, 20))
        self.LE_contra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_contra.setText("")
        self.LE_contra.setObjectName("LE_contra")
        InicioSesion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InicioSesion)
        self.statusbar.setObjectName("statusbar")
        InicioSesion.setStatusBar(self.statusbar)

        self.retranslateUi(InicioSesion)
        
        QtCore.QMetaObject.connectSlotsByName(InicioSesion)

    def retranslateUi(self, InicioSesion):
        _translate = QtCore.QCoreApplication.translate
        InicioSesion.setWindowTitle(_translate("InicioSesion", "Iniciar sesion"))
        self.btn_iniciar_sesion.setText(_translate("InicioSesion", "Iniciar sesión"))
        self.lbl_usuario.setText(_translate("InicioSesion", "Usuario:"))
        self.lbl_contra.setText(_translate("InicioSesion", "Contraseña:"))

class ErrorLogin(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Interfaz5.ui', self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InicioSesion = QtWidgets.QMainWindow()
    ui = Ui_InicioSesion()
    ui.setupUi(InicioSesion)
    InicioSesion.show()
    app.exec_()
