#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    QtWidgets.QMessageBox.critical(
        None, "Critique", "Je suis une boîte 'critical'")

    sys.exit(app.exec_())

