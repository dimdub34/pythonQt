#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.setLayout(QtWidgets.QVBoxLayout())  # mutateur
    w.setWindowTitle("Deuxième GUI")  # mutateur

    label = QtWidgets.QLabel()
    label.setText(w.windowTitle())  # mutateur + acesseur
    w.layout().addWidget(label)  # accesseur

    w.show()

    sys.exit(app.exec_())


