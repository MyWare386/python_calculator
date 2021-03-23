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
print(Fore.BLUE + Style.BRIGHT + "-> Made " + Style.RESET_ALL + Style.BRIGHT + "by " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "MyWare" + Style.RESET_ALL)
print("")
print("--------------------------------------------------")
print("")

# ------------------------------------------------------- Questions -------------------------------------------------------

questions = [
    {
        'type': 'list',
        'name': 'calcul',
        'message': 'What operation do you want to do ?',
        'choices': ['Addition +', 'Subtraction -', 'Multiplication *', 'Division /']
    },
    {
        'type': 'input',
        'name': 'a',
        'message': 'What\'s your first number ?',
    },
    {
        'type': 'input',
        'name': 'b',
        'message': 'What\'s your second number ?',
    },
    {
        'type': 'input',
        'name': 'c',
        'message': 'What\'s your third number ? (put 0 or 1 if you don\'t need this number)',
    },
    {
        'type': 'input',
        'name': 'd',
        'message': 'What\'s your fourth number ? ? (put 0 or 1 if you don\'t need this number)',
    },
    {
        'type': 'input',
        'name': 'e',
        'message': 'What\'s your fifth number ? (put 0 or 1 if you don\'t need this number)',
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


if calcul == 'Addition +':
    print("")
    print("")
    print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
    print("")
    print(decimal_a + decimal_b + decimal_c + decimal_d + decimal_e)
else:
    if calcul == 'Subtraction -':
        print("")
        print("")
        print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
        print("")
        print(decimal_a - decimal_b - decimal_c - decimal_d - decimal_e)
    else:
        if calcul == 'Multiplication *':
            print("")
            print("")
            print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
            print("")
            print(decimal_a * decimal_b * decimal_c * decimal_d * decimal_e)
        else:
            if calcul == 'Division /':
                print("")
                print("")
                print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
                print("")
                print(decimal_a / decimal_b / decimal_c / decimal_d / decimal_e)


# ------------------------------------------------------- Fin -------------------------------------------------------

print("")
print("--------------------------------------------------")
print("")
input(Fore.RED + "ENTER to quit" + Style.RESET_ALL)
