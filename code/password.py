#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import pickle
from string import ascii_letters


currentdir = os.path.dirname(os.path.abspath(__file__))


def get_pass_dict(pickle_file):
    my_dict_pass = None
    if pickle_file in os.listdir(currentdir):
        with open(os.path.join(currentdir, pickle_file), "rb") as fichier:
            my_dict_pass = pickle.load(fichier)
    return my_dict_pass or {}


def create_password(word, nb_letters=3):
    if type(word) is not str:
        return create_password(str(word))
    txt = "!{}_".format(word[:3].lower())
    try:
        indexes = "".join(
            map(str, [ascii_letters.index(l.lower()) for l in word[:3]]))
    except ValueError:
        print("Il faut uniquement des lettres de l'alphabet pour "
                      "les {} premiers caractères".format(nb_letters))
        return None
    else:
        txt += indexes + "$"
        return txt


if __name__ == "__main__":
    word = input("Veuillez saisir un mot-clé: ")
    my_dict_pass = get_pass_dict(".pass.pck")
    if word not in my_dict_pass.keys():
        pwd = create_password(word)
        if pwd is None:
            sys.exit(0)
        my_dict_pass[word] = create_password(word)
        with open(os.path.join(currentdir, ".pass.pck"), "wb") as fichier:
            pickle.dump(my_dict_pass, fichier)
    print("Le mot de passe pour {} est : {}".format(word, my_dict_pass[word]))



