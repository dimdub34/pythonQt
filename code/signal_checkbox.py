#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout()
        self.setLayout(self.form)

        self.checkbox = QCheckBox()
        self.form.addRow(QLabel("Cocher si Qt c'est bien"), self.checkbox)
        self.checkbox.stateChanged.connect(self.display_value)  # stateChanged envoie l'état (Qt.Checked ou Qt.Unchecked)

        self.label = QLabel("Non")
        self.form.addRow(QLabel("Résultat"), self.label)

    def display_value(self, state):
        if state == Qt.Checked:
            self.label.setText("Oui")
        elif state == Qt.Unchecked:
            self.label.setText("Non")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MyWidget()
    wid.show()
    sys.exit(app.exec_())
