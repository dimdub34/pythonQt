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
        self.menuBar().addMenu(self.menu_fichier)
        self.menu_edition = QMenu("Edition")
        self.menuBar().addMenu(self.menu_edition)
        self.menu_outils = QMenu("Outils")
        self.menuBar().addMenu(self.menu_outils)

        # il faut un widget en élément principal
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        # un label
        self.label = QLabel("Ceci est une fenêtre avec un menu")
        self.layout.addWidget(self.label, 0, Qt.AlignLeft)

        self.setMinimumWidth(30)
        self.setWindowTitle("QMainWindow")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyMainWindow()
    wid.show()

    sys.exit(app.exec_())
