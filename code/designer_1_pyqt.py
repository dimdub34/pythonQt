#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import designer_1

class MyDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        
        self.ui = designer_1.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.label_nom.setText("Votre nom")
        self.ui.label_prenom.setText(u"Votre prénom")
        self.ui.label_genre.setText("Votre genre")
        self.ui.radioButton_homme.setText("Homme")
        self.ui.radioButton_femme.setText("Femme")
        
        self.ui.buttonBox.accepted.connect(self._accept)
        self.ui.buttonBox.rejected.connect(self.reject)
    
    def _accept(self):
        try:
            nom = str(self.ui.lineEdit_nom.text())
            prenom = str(self.ui.lineEdit_prenom.text())
            if not (nom or prenom):
                raise ValueError(u"Il faut entrer votre nom et votre prénom")
            if not (self.ui.radioButton_homme.isChecked() or 
            self.ui.radioButton_femme.isChecked()):
                raise ValueError(u"Vous devez préciser votre genre")
            else:
                homme = self.ui.radioButton_homme.isChecked()
        except ValueError as e:
            QtGui.QMessageBox.warning(self, "Attention", e.message)
            return
        
        QtGui.QMessageBox.information(self, u"Résumé", 
        u"Vous vous appelez {} {} et vous êtes {}".format(
        prenom.capitalize(), nom.upper(), "un homme" if homme else "une femme"))
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_dialog = MyDialog()
    my_dialog.show()
    sys.exit(app.exec_())
