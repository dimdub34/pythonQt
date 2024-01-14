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

        self.button = QDialogButtonBox(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        self.layout.addWidget(self.button)

        self.setWindowTitle("Widgets")
        self.adjustSize()

    def reject(self):
        confirmation = QMessageBox.question(
            self, "Confirmation", "Quitter l'application?",
            QMessageBox.No | QMessageBox.Yes)
        if confirmation != QMessageBox.Yes:
            return
        else:
            super().reject()

    def accept(self):
        try:

            plat = self.lineEdit_plat.text()
            if not plat:
                raise ValueError("Vous devez saisir un plat")

            try:
                forme = self.radio_group.checkedButton().text()
            except AttributeError:
                raise ValueError("Vous devez cocher une forme")

            couleur = self.combo.currentText()
            if couleur == "Choisir":
                raise ValueError("Vous devez choisir une couleur")

            legumes = [c.text() for c in self.checkbox_list if c.isChecked()]

            comment = self.textEdit_comments.toPlainText()

        except ValueError as e:
            QMessageBox.warning(self, "Attention", "{}".format(e))
            return

        QMessageBox.information(
            self, "Saisies",
            "Plat: {}\nforme: {}\ncouleur: {}\nlégume(s): {}\n"
            "Commentaire: {}".format(plat, forme, couleur, legumes, comment))
        confirmation = QMessageBox.question(
            self, "Confirmation", "Vous confirmez?", QMessageBox.No | QMessageBox.Yes)
        if confirmation != QMessageBox.Yes:
            return
        super().accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyWidget()
    wid.show()

    sys.exit(app.exec_())
