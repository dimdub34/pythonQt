#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
import designer_1


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = designer_1.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Designer")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywid = MyWidget()
    mywid.show()
    sys.exit(app.exec_())

