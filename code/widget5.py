#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.form = QtWidgets.QFormLayout()
        self.layout.addLayout(self.form)

        self.lineEdit_nom = QtWidgets.QLineEdit()
        self.form.addRow(QtWidgets.QLabel("Nom"), self.lineEdit_nom)

        self.lineEdit_prenom = QtWidgets.QLineEdit()
        self.form.addRow(QtWidgets.QLabel("Prénom"), self.lineEdit_prenom)

        self.naissance_date = QtWidgets.QDateEdit()
        self.form.addRow(QtWidgets.QLabel("Date de naissance"),
                         self.naissance_date)

        self.button = QtWidgets.QPushButton("Ok")
        self.layout.addWidget(self.button, 0, QtCore.Qt.AlignRight)

        self.setWindowTitle("Form Layout")
        self.adjustSize()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wid = MyWidget()
    wid.show()
    sys.exit(app.exec_())
