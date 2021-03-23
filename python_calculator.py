# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import regex

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

import colorama
from colorama import Fore
from colorama import Style

from decimal import *


style = style_from_dict({
    Token.QuestionMark: '#33CC00 bold',
    Token.Selected: '#33CC00 bold', #default
    Token.Instruction: '',  # default
    Token.Answer: '#33CC00 bold',
    Token.Question: '',
})


colorama.init()
print(Fore.GREEN + Style.BRIGHT + "-> Python Calculator" + Style.RESET_ALL)
print("")
print(Fore.BLUE + Style.BRIGHT + "-> Créé " + Style.RESET_ALL + Style.BRIGHT + "par " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "MyWare" + Style.RESET_ALL)
print("")
print("--------------------------------------------------")
print("")

# ------------------------------------------------------- Questions -------------------------------------------------------

questions = [
    {
        'type': 'list',
        'name': 'calcul',
        'message': 'Quel type de calcul voulez-vous faire ?',
        'choices': ['Une addition +', 'Une soustraction -', 'Une multiplication *', 'Une division /']
    },
    {
        'type': 'input',
        'name': 'a',
        'message': 'Quel est votre premier nombre ?',
    },
    {
        'type': 'input',
        'name': 'b',
        'message': 'Quel est votre deuxième nombre ?',
    },
    {
        'type': 'input',
        'name': 'c',
        'message': 'Quel est votre troisième nombre ? (mettez 0 ou 1 (pour les divisions) si vous n\'avez pas besoin de ce nombre)',
    },
    {
        'type': 'input',
        'name': 'd',
        'message': 'Quel est votre quatrième nombre ? (mettez 0 ou 1 (pour les divisions) si vous n\'avez pas besoin de ce nombre)',
    },
    {
        'type': 'input',
        'name': 'e',
        'message': 'Quel est votre cinquième nombre ? (mettez 0 ou 1 (pour les divisions) si vous n\'avez pas besoin de ce nombre)',
    }
]

# ------------------------------------------------------- Calcul -------------------------------------------------------

answers = prompt(questions, style=style)


calcul = answers['calcul']


a = answers['a']

decimal_a = Decimal(a)


b = answers['b']

decimal_b = Decimal(b)


c = answers['c']

decimal_c = Decimal(c)


d = answers['d']

decimal_d = Decimal(d)


e = answers['e']

decimal_e = Decimal(e)


if calcul == 'Une addition +':
    print("")
    print("")
    print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
    print("")
    print(decimal_a + decimal_b + decimal_c + decimal_d + decimal_e)
else:
    if calcul == 'Une soustraction -':
        print("")
        print("")
        print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
        print("")
        print(decimal_a - decimal_b - decimal_c - decimal_d - decimal_e)
    else:
        if calcul == 'Une multiplication *':
            print("")
            print("")
            print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
            print("")
            print(decimal_a * decimal_b * decimal_c * decimal_d * decimal_e)
        else:
            if calcul == 'Une division /':
                print("")
                print("")
                print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
                print("")
                print(decimal_a / decimal_b / decimal_c / decimal_d / decimal_e)


# ------------------------------------------------------- Fin -------------------------------------------------------

print("")
print("--------------------------------------------------")
print("")
input(Fore.RED + "Appuyez sur ENTRÉE pour terminer le programme." + Style.RESET_ALL)
