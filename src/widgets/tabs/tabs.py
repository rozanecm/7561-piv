# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/widgets/tabs/tabs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.agregar_punto_button = QtWidgets.QPushButton(Form)
        self.agregar_punto_button.setObjectName("agregar_punto_button")
        self.horizontalLayout_7.addWidget(self.agregar_punto_button)
        self.quitar_punto_button = QtWidgets.QPushButton(Form)
        self.quitar_punto_button.setEnabled(False)
        self.quitar_punto_button.setObjectName("quitar_punto_button")
        self.horizontalLayout_7.addWidget(self.quitar_punto_button)
        self.restablecer_button = QtWidgets.QPushButton(Form)
        self.restablecer_button.setObjectName("restablecer_button")
        self.horizontalLayout_7.addWidget(self.restablecer_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(-1)
        self.quitar_punto_button.clicked.connect(Form.remove_marker)
        self.agregar_punto_button.clicked.connect(Form.add_marker)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.agregar_punto_button.setText(_translate("Form", "Agregar punto"))
        self.quitar_punto_button.setText(_translate("Form", "Quitar punto"))
        self.restablecer_button.setText(_translate("Form", "Restablecer"))
