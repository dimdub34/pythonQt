#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout()
        self.setLayout(self.form)

        self.radio_layout = QHBoxLayout()
        self.radio_group = QButtonGroup()

        self.radio_homme = QRadioButton("Homme")
        self.radio_group.addButton(self.radio_homme)
        self.radio_layout.addWidget(self.radio_homme)

        self.radio_femme = QRadioButton("Femme")
        self.radio_group.addButton(self.radio_femme)
        self.radio_layout.addWidget(self.radio_femme)

        self.form.addRow(QLabel("Genre"), self.radio_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyWidget()
    wid.show()

    sys.exit(app.exec_())
