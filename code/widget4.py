#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel()
        self.label.setText("ici mon label 1")
        self.layout.addWidget(self.label)

        self.label1 = QtWidgets.QLabel()
        self.label1.setText("ici mon label 2")
        self.layout.addWidget(self.label1)

        self.setWindowTitle("Layout vertical")
        self.setMinimumWidth(200)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wid = MyWidget()
    wid.show()
    sys.exit(app.exec_())
