#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.setWindowTitle("Premier GUI")

    layout = QtWidgets.QVBoxLayout()
    w.setLayout(layout)

    label = QtWidgets.QLabel("Ceci est mon premier label")
    layout.addWidget(label)

    w.show()

    sys.exit(app.exec_())

