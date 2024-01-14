# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 143)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_nom = QtWidgets.QLabel(Form)
        self.label_nom.setObjectName("label_nom")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nom)
        self.lineEdit_nom = QtWidgets.QLineEdit(Form)
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nom)
        self.label_prenom = QtWidgets.QLabel(Form)
        self.label_prenom.setObjectName("label_prenom")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_prenom)
        self.lineEdit_prenom = QtWidgets.QLineEdit(Form)
        self.lineEdit_prenom.setObjectName("lineEdit_prenom")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_prenom)
        self.label_genre = QtWidgets.QLabel(Form)
        self.label_genre.setObjectName("label_genre")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_genre)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_homme = QtWidgets.QRadioButton(Form)
        self.radioButton_homme.setObjectName("radioButton_homme")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_homme)
        self.horizontalLayout.addWidget(self.radioButton_homme)
        self.radioButton_femme = QtWidgets.QRadioButton(Form)
        self.radioButton_femme.setObjectName("radioButton_femme")
        self.buttonGroup.addButton(self.radioButton_femme)
        self.horizontalLayout.addWidget(self.radioButton_femme)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_nom.setText(_translate("Form", "Votre nom"))
        self.label_prenom.setText(_translate("Form", "Votre prénom"))
        self.label_genre.setText(_translate("Form", "Votre genre"))
        self.radioButton_homme.setText(_translate("Form", "Homme"))
        self.radioButton_femme.setText(_translate("Form", "Femme"))

