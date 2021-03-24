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
        'choices': ['Addition +', 'Subtraction -', 'Multiplication *', 'Division /', 'Square root √ (the programme will use your first number)']
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
    }
]

# ------------------------------------------------------- Calcul -------------------------------------------------------

answers = prompt(questions, style=style)


calcul = answers['calcul']


a = answers['a']

decimal_a = Decimal(a)


b = answers['b']

decimal_b = Decimal(b)


if calcul == 'Addition +':
    print("")
    print("")
    print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
    print("")
    print(decimal_a + decimal_b)
else:
    if calcul == 'Subtraction -':
        print("")
        print("")
        print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
        print("")
        print(decimal_a - decimal_b)
    else:
        if calcul == 'Multiplication *':
            print("")
            print("")
            print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
            print("")
            print(decimal_a * decimal_b)
        else:
            if calcul == 'Division /':
                print("")
                print("")
                print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
                print("")
                print(decimal_a / decimal_b)
            else:
                if calcul == 'Square root √ (the programme will use your first number)':
                    print("")
                    print("")
                    print(Fore.GREEN + Style.BRIGHT + "Result = " + Style.RESET_ALL)
                    print("")
                    print(math.sqrt(decimal_a))


# ------------------------------------------------------- Fin -------------------------------------------------------

print("")
print("--------------------------------------------------")
print("")
input(Fore.RED + "ENTER to quit" + Style.RESET_ALL)
