#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # barre de menu
        self.setMenuBar(QMenuBar())
        self.menu_fichier = QMenu("Fichier")
        self.action_fichier = QAction("Quitter")
        self.action_fichier.triggered.connect(sys.exit)
        self.menu_fichier.addAction(self.action_fichier)
        self.menuBar().addMenu(self.menu_fichier)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyMainWindow()
    wid.show()

    sys.exit(app.exec_())
