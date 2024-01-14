#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class MyDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        
        mybutton = QtGui.QPushButton("My first button")
        mybutton_layout = QtGui.QHBoxLayout()
        mybutton_layout.addSpacerItem(
        QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, 
        QtGui.QSizePolicy.Expanding))
        mybutton_layout.addWidget(mybutton)
        mybutton_layout.addSpacerItem(
        QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, 
        QtGui.QSizePolicy.Expanding))
        layout.addLayout(mybutton_layout)
        
        self.setFixedSize(500, 500)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    wind = MyDialog()
    wind.show()
    sys.exit(app.exec_())
