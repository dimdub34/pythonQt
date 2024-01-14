#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    confirmation = QtWidgets.QMessageBox.question(
        None, "Question", "Vous confirmez votre choix?",
        QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)

    sys.exit(app.exec_())

