#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    QtWidgets.QMessageBox.warning(
        None, "Attention", "Je suis une boîte de warning")

    sys.exit(app.exec_())

