# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/widgets/tabsContent/tab_content.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabContent(object):
    def setupUi(self, TabContent):
        TabContent.setObjectName("TabContent")
        TabContent.resize(598, 436)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TabContent)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tamano_de_seleccion_groupBox = QtWidgets.QGroupBox(TabContent)
        self.tamano_de_seleccion_groupBox.setObjectName("tamano_de_seleccion_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tamano_de_seleccion_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.x8_radioButton = QtWidgets.QRadioButton(self.tamano_de_seleccion_groupBox)
        self.x8_radioButton.setObjectName("x8_radioButton")
        self.verticalLayout.addWidget(self.x8_radioButton)
        self.x16_radioButton = QtWidgets.QRadioButton(self.tamano_de_seleccion_groupBox)
        self.x16_radioButton.setObjectName("x16_radioButton")
        self.verticalLayout.addWidget(self.x16_radioButton)
        self.x32_radioButton = QtWidgets.QRadioButton(self.tamano_de_seleccion_groupBox)
        self.x32_radioButton.setObjectName("x32_radioButton")
        self.verticalLayout.addWidget(self.x32_radioButton)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.otro_radioButton = QtWidgets.QRadioButton(self.tamano_de_seleccion_groupBox)
        self.otro_radioButton.setObjectName("otro_radioButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.otro_radioButton)
        self.tamano_de_seleccion_spinBox = QtWidgets.QSpinBox(self.tamano_de_seleccion_groupBox)
        self.tamano_de_seleccion_spinBox.setEnabled(True)
        self.tamano_de_seleccion_spinBox.setObjectName("tamano_de_seleccion_spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tamano_de_seleccion_spinBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addWidget(self.tamano_de_seleccion_groupBox)
        self.posicion_groupBox = QtWidgets.QGroupBox(TabContent)
        self.posicion_groupBox.setObjectName("posicion_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.posicion_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pos_x_label = QtWidgets.QLabel(self.posicion_groupBox)
        self.pos_x_label.setObjectName("pos_x_label")
        self.horizontalLayout_3.addWidget(self.pos_x_label)
        self.pos_x_spinBox = QtWidgets.QSpinBox(self.posicion_groupBox)
        self.pos_x_spinBox.setMaximum(9999)
        self.pos_x_spinBox.setObjectName("pos_x_spinBox")
        self.horizontalLayout_3.addWidget(self.pos_x_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pos_y_label = QtWidgets.QLabel(self.posicion_groupBox)
        self.pos_y_label.setObjectName("pos_y_label")
        self.horizontalLayout_8.addWidget(self.pos_y_label)
        self.pos_y_spinBox = QtWidgets.QSpinBox(self.posicion_groupBox)
        self.pos_y_spinBox.setMaximum(9999)
        self.pos_y_spinBox.setObjectName("pos_y_spinBox")
        self.horizontalLayout_8.addWidget(self.pos_y_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addWidget(self.posicion_groupBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(299, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(TabContent)
        QtCore.QMetaObject.connectSlotsByName(TabContent)

    def retranslateUi(self, TabContent):
        _translate = QtCore.QCoreApplication.translate
        TabContent.setWindowTitle(_translate("TabContent", "Form"))
        self.tamano_de_seleccion_groupBox.setTitle(_translate("TabContent", "Tamaño de selección"))
        self.x8_radioButton.setText(_translate("TabContent", "8x8"))
        self.x16_radioButton.setText(_translate("TabContent", "16x16"))
        self.x32_radioButton.setText(_translate("TabContent", "32x32"))
        self.otro_radioButton.setText(_translate("TabContent", "otro"))
        self.posicion_groupBox.setTitle(_translate("TabContent", "Posicion"))
        self.pos_x_label.setText(_translate("TabContent", "x:"))
        self.pos_y_label.setText(_translate("TabContent", "y:"))
