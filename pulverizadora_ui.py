# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pulverizadoraUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 132, 405, 361))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.caudal_de_campo = QtWidgets.QLabel(self.frame)
        self.caudal_de_campo.setGeometry(QtCore.QRect(11, 11, 271, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.caudal_de_campo.setFont(font)
        self.caudal_de_campo.setObjectName("caudal_de_campo")
        self.caudal_de_boquilla = QtWidgets.QLabel(self.frame)
        self.caudal_de_boquilla.setGeometry(QtCore.QRect(11, 45, 267, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.caudal_de_boquilla.setFont(font)
        self.caudal_de_boquilla.setObjectName("caudal_de_boquilla")
        self.velocidad_de_avance = QtWidgets.QLabel(self.frame)
        self.velocidad_de_avance.setGeometry(QtCore.QRect(11, 79, 222, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.velocidad_de_avance.setFont(font)
        self.velocidad_de_avance.setObjectName("velocidad_de_avance")
        self.ancho_labor_boquilla = QtWidgets.QLabel(self.frame)
        self.ancho_labor_boquilla.setGeometry(QtCore.QRect(11, 113, 290, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.ancho_labor_boquilla.setFont(font)
        self.ancho_labor_boquilla.setObjectName("ancho_labor_boquilla")
        self.resultados = QtWidgets.QLabel(self.frame)
        self.resultados.setGeometry(QtCore.QRect(10, 210, 371, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultados.setFont(font)
        self.resultados.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultados.setObjectName("resultados")
        self.caja_caudal_campo = QtWidgets.QLineEdit(self.frame)
        self.caja_caudal_campo.setGeometry(QtCore.QRect(307, 11, 87, 28))
        self.caja_caudal_campo.setObjectName("caja_caudal_campo")
        self.caja_caudal_boquilla = QtWidgets.QLineEdit(self.frame)
        self.caja_caudal_boquilla.setGeometry(QtCore.QRect(307, 45, 87, 28))
        self.caja_caudal_boquilla.setObjectName("caja_caudal_boquilla")
        self.caja_velocidad_avance = QtWidgets.QLineEdit(self.frame)
        self.caja_velocidad_avance.setGeometry(QtCore.QRect(307, 79, 87, 28))
        self.caja_velocidad_avance.setObjectName("caja_velocidad_avance")
        self.caja_ancho_labor_boquilla = QtWidgets.QLineEdit(self.frame)
        self.caja_ancho_labor_boquilla.setGeometry(QtCore.QRect(307, 113, 87, 28))
        self.caja_ancho_labor_boquilla.setObjectName("caja_ancho_labor_boquilla")
        self.boton_calcular = QtWidgets.QPushButton(self.frame)
        self.boton_calcular.setGeometry(QtCore.QRect(10, 150, 111, 41))
        self.boton_calcular.setObjectName("boton_calcular")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 391, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 235, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.caudal_de_campo.setText(_translate("MainWindow", "Caudal de campo (Q) [litros/hectárea]"))
        self.caudal_de_boquilla.setText(_translate("MainWindow", "Caudal de boquilla (q) [litros/minuto]"))
        self.velocidad_de_avance.setText(_translate("MainWindow", "Velocidad de avance [km/hora]"))
        self.ancho_labor_boquilla.setText(_translate("MainWindow", "Ancho de labor de cada boquilla [metro]"))
        self.resultados.setText(_translate("MainWindow", "Resultados"))
        self.boton_calcular.setText(_translate("MainWindow", "Calcular"))
        self.label.setText(_translate("MainWindow", "Cálculo para la calibración de pulverizadoras"))
        self.label_2.setText(_translate("MainWindow", "Dejar vacía la caja con el valor a calcular:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())