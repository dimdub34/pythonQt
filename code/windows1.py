#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class MyDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.form = QFormLayout()
        self.layout.addLayout(self.form)

        self.lineEdit_nom = QLineEdit()
        self.form.addRow(QLabel("Nom"), self.lineEdit_nom)

        self.lineEdit_prenom = QLineEdit()
        self.form.addRow(QLabel("Prénom"), self.lineEdit_prenom)

        self.button = QDialogButtonBox(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.layout.addWidget(self.button)

        self.setWindowTitle("QDialog")
        self.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyDialog(None)
    result = w.exec_()
    print(result)

    sys.exit(app.exec_())
