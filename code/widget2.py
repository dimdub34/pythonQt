#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


class MyWidget(QtWidgets.QWidget):  # hérite de la classe QWidget
    def __init__(self):
        super().__init__()  # instantiation de la classe mère

        self.setWindowTitle("Troisième GUI")
        self.setLayout(QtWidgets.QVBoxLayout())

        self.label = QtWidgets.QLabel("Ceci est mon troisième label")
        self.layout().addWidget(self.label)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())


