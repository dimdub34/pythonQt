#! /usr/bin/env python3

import pickle
import sys
from PyQt5 import QtWidgets
import passwd


def get_dict():
    try:
        with open("passwords.pck", "rb") as f:
            the_dict = pickle.load(f)
    except IOError:
        with open("passwords.pck", "wb") as f:
            pickle.dump({}, f)
        return get_dict()
    return the_dict


def save_dict(the_dict):
    with open("passwords.pck", "wb") as f:
        pickle.dump(the_dict, f)


def get_passwd(le_mot, nb_lettres=4):
    the_dict = get_dict()
    if le_mot in the_dict.keys():
        print("Le mot de passe existe déjà")
        return the_dict[le_mot]
    else:
        try:
            mot = le_mot[:nb_lettres]
            count_lettres = [le_mot.count(l) for l in mot]
            le_password = f"!{mot.upper()}_{''.join(map(str, count_lettres))}=$"
        except (TypeError, AttributeError):
            return "Il faut passer une chaîne de caractère en argument"
        else:
            print("Enregistrement du mot de passe")
            the_dict[le_mot] = le_password
            save_dict(the_dict)
            return le_password


class Password(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = passwd.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.display_passwd)

    def display_passwd(self):
        the_mot = self.ui.lineEdit.text()
        self.ui.label_out.setText(get_passwd(the_mot))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetre = Password()
    fenetre.show()
    sys.exit(app.exec_())
