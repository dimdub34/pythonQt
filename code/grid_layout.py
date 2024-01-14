#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)

        self.grid.addWidget(QLabel("Nom"), 0, 0)
        self.lineEdit_nom = QLineEdit()
        self.grid.addWidget(self.lineEdit_nom, 0, 1)

        self.grid.addWidget(QLabel("Prénom"), 0, 2)
        self.lineEdit_prenom = QLineEdit()
        self.grid.addWidget(self.lineEdit_prenom, 0, 3)

        self.grid.addWidget(QLabel("Date de naissance"), 1, 0)
        self.naissance_date = QDateEdit()
        self.grid.addWidget(self.naissance_date, 1, 1)

        self.button = QDialogButtonBox(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.layout.addWidget(self.button)

        self.setWindowTitle("Grid Layout")
        self.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyWidget()
    wid.show()

    sys.exit(app.exec_())
