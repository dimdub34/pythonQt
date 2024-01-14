#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
from random import choice


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        form = QtWidgets.QFormLayout()
        self.setLayout(form)

        self._checkbox = QtWidgets.QCheckBox()
        form.addRow(QtWidgets.QLabel("Cocher si Qt c'est bien"), self._checkbox)
        self._checkbox.stateChanged.connect(self._display_value)

        self._label = QtWidgets.QLabel("Non")
        form.addRow(QtWidgets.QLabel("Résultat"), self._label)

        self.setWindowTitle("My Widget")
        self.adjustSize()

    def _display_value(self):
        if self._checkbox.isChecked():
            self._label.setText("Oui")
        elif not self._checkbox.isChecked():
            self._label.setText("Non")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wid = MyWidget()
    wid.show()
    sys.exit(app.exec_())
