#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())

        self.lineEdit = QLineEdit("Ceci est un lineEdit")
        self.layout().addWidget(self.lineEdit)

        self.textEdit = QTextEdit()
        self.textEdit.setHtml("<p>Ceci est un <b>textEdit</b>, il accepte "
                               "le html")
        self.textEdit.setMaximumHeight(150)
        self.layout().addWidget(self.textEdit)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyWidget()
    wid.show()

    sys.exit(app.exec_())
