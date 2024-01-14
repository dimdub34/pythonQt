#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dossier = QtWidgets.QFileDialog.getExistingDirectory(
        None, caption="Choisir un dossier",
        directory="/home/dimitri/Documents/travail/CFI2L/cours/python")
    if dossier:
        QtWidgets.QMessageBox.information(
            None, "Dossier", "Dossier choisi: {}".format(dossier))
    sys.exit(0)
