#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from random import choice


class MyWidgetSignal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Example signal bouton")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("Cliquer sur le bouton ci-dessous"))

        self.button = QPushButton("Cliquez-moi")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.dit_bonjour)

        self.label_out = QLabel()
        self.layout.addWidget(self.label_out)

    def dit_bonjour(self):
        self.label_out.setText("Hello world!")



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.colors = ["black", "blue", "yellow", "brown", "red", "pink"]
        self.current_color_index = 0

        self.setLayout(QVBoxLayout())

        self.label = QLabel("Bonjour tout le monde")
        self.label.setStyleSheet("color: {}".format(self.colors[self.current_color_index]))
        self.layout().addWidget(self.label)

        self.button = QPushButton("Changer la couleur")
        self.button.clicked.connect(self.change_color)
        self.layout().addWidget(self.button)

    def change_color(self):
        self.current_color_index += 1
        if self.current_color_index == len(self.colors) - 1:
            self.current_color_index = 0
        self.label.setStyleSheet("color: {}".format(self.colors[self.current_color_index]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MyWidgetSignal()
    wid.show()
    sys.exit(app.exec_())
