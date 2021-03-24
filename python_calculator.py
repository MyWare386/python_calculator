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

import math


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
        'message': 'Quel opération voulez-vous faire ?',
        'choices': ['Une addition +', 'Une soustraction -', 'Une multiplication *', 'Une division /', 'Une racine carré √ (seul le premier nombre entré sera pris en compte)']
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
    }
]

# ------------------------------------------------------- Calcul -------------------------------------------------------

answers = prompt(questions, style=style)


calcul = answers['calcul']


a = answers['a']

decimal_a = Decimal(a)


b = answers['b']

decimal_b = Decimal(b)


if calcul == 'Une addition +':
    print("")
    print("")
    print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
    print("")
    print(decimal_a + decimal_b)
else:
    if calcul == 'Une soustraction -':
        print("")
        print("")
        print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
        print("")
        print(decimal_a - decimal_b)
    else:
        if calcul == 'Une multiplication *':
            print("")
            print("")
            print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
            print("")
            print(decimal_a * decimal_b)
        else:
            if calcul == 'Une division /':
                print("")
                print("")
                print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
                print("")
                print(decimal_a / decimal_b)
            else:
                if calcul == 'Une racine carré √ (seul le premier nombre entré sera pris en compte)':
                    print("")
                    print("")
                    print(Fore.GREEN + Style.BRIGHT + "Résultat = " + Style.RESET_ALL)
                    print("")
                    print(math.sqrt(decimal_a))


# ------------------------------------------------------- Fin -------------------------------------------------------

print("")
print("--------------------------------------------------")
print("")
input(Fore.RED + "Appuyez sur ENTRÉE pour terminer le programme." + Style.RESET_ALL)
