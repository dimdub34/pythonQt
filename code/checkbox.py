#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout()
        self.setLayout(self.form)

        self.checkbox_layout = QHBoxLayout()

        self.checkbox_1 = QCheckBox("case 1")
        self.checkbox_layout.addWidget(self.checkbox_1)
        self.checkbox_2 = QCheckBox("case 2")
        self.checkbox_layout.addWidget(self.checkbox_2)
        self.checkbox_3 = QCheckBox("case 3")
        self.checkbox_layout.addWidget(self.checkbox_3)

        self.checkbox_layout.addStretch()  # pour que les checkbox s'alignent à gauche
        self.form.addRow(QLabel("Cases à cocher"), self.checkbox_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyWidget()
    wid.show()

    sys.exit(app.exec_())
