#! /usr/bin/env python33
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QtWidgets.QVBoxLayout())

        self.img = QtGui.QPixmap("../img/logo.png")
        self.img = self.img.scaledToWidth(200)
        self.label = QtWidgets.QLabel()
        self.label.setPixmap(self.img)
        self.layout().addWidget(self.label)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wid = MyWidget()
    wid.show()
    sys.exit(app.exec_())
