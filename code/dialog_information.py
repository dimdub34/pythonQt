#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    QtWidgets.QMessageBox.information(
        None, "Information", "Je suis une boîte d'information")

    sys.exit(app.exec_())

