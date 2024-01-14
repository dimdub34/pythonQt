#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    fichier, _ = QtWidgets.QFileDialog.getSaveFileName(
        None, caption="Choisir un fichier",
        directory="/home/dimitri/Documents/travail/CFI2L/cours/python/pyqt")
    if fichier:
        QtWidgets.QMessageBox.information(
            None, "Fichier", "Fichier choisi: {}".format(fichier))
    sys.exit(0)
