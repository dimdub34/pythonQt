#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


class DPassword(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # barre de menu
        self._menu_bar = QtWidgets.QMenuBar()
        self.setMenuBar(self._menu_bar)
        self._menu_fichier = QtWidgets.QMenu("Fichier")
        self._action_display = QtWidgets.QAction("Afficher les mots de passe")
        self._menu_fichier.addAction(self._action_display)
        self._action_display.triggered.connect(self._display_passwords)


        # contenu écran

        self._main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self._main_widget)

        self._layout = QtWidgets.QVBoxLayout()
        self._main_widget.setLayout(self._layout)
