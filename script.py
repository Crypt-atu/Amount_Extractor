#!/bin/python3
'''
AUTHOR: CRYPT_ATU
NAME: AMOUNT EXTRACTOR.v1
'''

#Necessary Import
import sys
import os
import time
from colorama import init, Fore, Style

#Initialize colorama for Windows support
init(autoreset=True)

#TypeWritter Function
def typewriter_func(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    print()

#Banner Function
def banner():
    print(Fore.GREEN + '''
    -------------------------------------------\n
    |   AUTHOR: CRYPT_ATU                      |\n
    |   NAME: AMOUNT EXTRACTOR.v1              |\n
    |                                          |\n
    -------------------------------------------
    ''')
print()
print()



try:
    #Intro Banners
    typewriter_func("LOADING AMOUT_EXTRACTOR.v1»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»", color=Fore.GREEN, delay=0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    print()
    print()
    typewriter_func("AMOUNT EXTRACTOR: The main aim of this is to calculate the amounts you have in a stream of text and give you an output based on the option you pick.", color=Fore.YELLOW)
    typewriter_func("NOTE: Make sure the values you intend to calculate has a Currency Symbol in front of it to indicate its a money value.", color=Fore.RED)

    typewriter_func("Paste your text. Press Ctrl+D(Linux/Mac) or Ctrl+Z(Windows) then Enter to end.", color=Fore.CYAN)

    #Collect Sentence from User
    sentence = sys.stdin.read()

    #Stores famous currency symbols
    currency_symbols = list('₤₦€¥$')

    word_in_sentence = sentence.split()


    amount = []

    current_currency = " "
    for word in word_in_sentence:
        if word[0] in currency_symbols:
            current_currency = word[0]
            word = word[1:]
            clean_numbers = word.replace(',','')
            amount.append(clean_numbers)


    #Functions to be performed
    def add_func(amount):
        summation = 0
        for value in amount:
            summation = summation + int(value)
        return summation

    def multiply_func(amount):
        product = 1
        for value in amount:
            product = product * int(value)
        return product

    def average_func(amount):
        num = len(amount)
        summation = add_func(amount)
        average = summation / num
        return average

    #Clear Screen
    os.system('cls' if os.name == 'nt' else 'clear')

    #keep Option in Loop
    #Function call
    while True:
        print()
        choice = input(Fore.MAGENTA + '''Choose the action of choice to do with the numbers:\n
        1). Adding the values.\n
        2). Multiplying the values.\n
        3). Getting the Average of the values.\n
        4). Exit.\n
Choice>>>>''' + Style.RESET_ALL)

        print()
        if choice == '1':
            summation = add_func(amount)
            print(Fore.BLUE + Style.BRIGHT + f'{len(amount)} Values Calculated' + Style.RESET_ALL)
            print(Fore.BLUE + Style.BRIGHT + f'Answer:{current_currency}{summation:,}' + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '2':
            product = multiply_func(amount)
            print(Fore.BLUE + Style.BRIGHT + f'{len(amount)} Values Calculated' + Style.RESET_ALL)
            print(Fore.BLUE + Style.BRIGHT + f'Answer:{current_currency}{product:,}' + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '3':
            average = average_func(amount)
            print(Fore.BLUE + Style.BRIGHT + f'{len(amount)} Values Calculated' + Style.RESET_ALL)
            print(Fore.BLUE + Style.BRIGHT + f'Answer:{current_currency}{average:,.2f}' + Style.RESET_ALL)
            time.sleep(1)
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            typewriter_func("Closing AMOUNT EXTRACTOR.v1================", color = Fore.CYAN, delay=0.1)
            time.sleep(1)
            typewriter_func("Author: Crypt_atu.", color = Fore.YELLOW, delay=0.1)
            typewriter_func("Phone_no: 08136602086.", color = Fore.YELLOW, delay=0.1)
            typewriter_func("Have a Nice Day!!!", color = Fore.YELLOW, delay=0.1)
            break
        else:
            print('Invalid Option. Input the correct option given')

except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter_func("\nInterrupt detected . Logging Out.....", color = Fore.RED, delay=0.1)
    time.sleep(1)
    typewriter_func("Author: Crypt_atu.", color = Fore.YELLOW, delay=0.1)
    typewriter_func("Phone_no: 08136602086.", color = Fore.YELLOW, delay=0.1)
    typewriter_func("Have a Nice Day!!!", color = Fore.YELLOW, delay=0.1)
    