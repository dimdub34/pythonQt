#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.form = QFormLayout()
        self.layout.addLayout(self.form)

        # lineEdit
        self.lineEdit_plat = QLineEdit()
        self.lineEdit_plat.setMaximumWidth(200)
        self.form.addRow(QLabel("Votre plat préféré"), self.lineEdit_plat)

        # radioButton
        self.radio_texts = ["Carré", "Losange", "Rectangle", "Rond", "Triangle"]
        self.radio_list = list()
        self.radio_group = QButtonGroup()
        self.radio_layout = QHBoxLayout()
        for i, r in enumerate(self.radio_texts):
            self.radio_list.append(QRadioButton(r))
            self.radio_group.addButton(self.radio_list[-1], i)
            self.radio_layout.addWidget(self.radio_list[-1])
        self.radio_layout.addStretch()
        self.form.addRow(QLabel("Sélectionner votre forme préférée"),
                         self.radio_layout)

        # comboBox
        self.combo_texts = ["Choisir", "Blanc", "Bleu", "Jaune", "Noir"]
        self.combo = QComboBox()
        self.combo.setMaximumWidth(100)
        self.combo.addItems(self.combo_texts)
        self.form.addRow(QLabel("Veuillez choisir votre couleur préférée"),
                         self.combo)

        # checkBox
        self.checkbox_texts = ["Aubergine", "Broccoli", "Carotte", "Choux fleur"]
        self.checkbox_list = list()
        self.chekbox_layout = QHBoxLayout()
        for p in self.checkbox_texts:
            self.checkbox_list.append(QCheckBox(p))
            self.chekbox_layout.addWidget(self.checkbox_list[-1])
        self.chekbox_layout.addStretch()
        self.form.addRow(QLabel("Cochez vos légumes préférés"), self.chekbox_layout)

        # textEdit
        self.textEdit_comments = QTextEdit()
        self.textEdit_comments.setMaximumSize(400, 200)
        self.form.addRow(QLabel("Laisser un commentaire"),
                         self.textEdit_comments)

        self._button = QDialogButtonBox(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.layout.addWidget(self._button)

        self.setWindowTitle("Widgets")
        self.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyWidget()
    wid.show()

    sys.exit(app.exec_())
