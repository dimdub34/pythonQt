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
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_dialog = MyDialog()
    my_dialog.show()
    sys.exit(app.exec_())
