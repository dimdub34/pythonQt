#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout()
        self.setLayout(self.form)

        self.combo_texts = ["Item 0", "Item 1", "Item 2", "Item 3"]
        self.combobox = QComboBox()
        self.combobox.addItems(self.combo_texts)
        self.form.addRow(QLabel("Liste déroulante"), self.combobox)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wid = MyWidget()
    wid.show()

    sys.exit(app.exec_())
