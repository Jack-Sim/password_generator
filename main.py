#!/usr/bin/env python3 

import sys
import random

VALID_INPUTS = ['l', 'u', 's', 'n']

char_options = {'l': 'abcdefghijklmnopqrstuvwxyz',
                'u': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                'n': '1234567890',
                's': '`¬!"£$%^&*()_-=+\{\}[];:@\'#/.>,<\|?~'}

def gen_password(criteria = 'l', password_length = 10):
    password = ''
    for i in range(password_length):
        character_pick = criteria[random.randrange(len(criteria))]
        password += random.choice(char_options[character_pick])
    
    return password



def error_message(n=0):
    if n == 0:
        print("[ERROR] - Not enough arguments, please refer to help menu using -h")
    elif n == 1:
        print("[ERROR] - Invalid options, please refer to help menu using -h")
    elif n == 2:
        print("[ERROR] - Too many parameters, please refer to help menu using -h")

def help_menu():
    print("----------------- Password Generator ------------------")
    print("$ A program to create passwords of different strenghts")
    print("-------------------------------------------------------")
    print("$ Usage Instructions")
    print(" ")
    print("$ Lowercase letters only")
    print("     pass_gen -l 10")
    print(" ")
    print("$ Lowercase and uppercase letters ")
    print("     pass_gen -lu 10")
    print(" ")
    print("$ Lowercase and uppercase letters and numbers")
    print("     pass_gen -lun 10")
    print(" ")
    print("$ Lowercase and uppercase letters, numbers and special chars")
    print("     pass_gen -luns 10")


def main():
    inputs = sys.argv
    if len(inputs) < 2:
        error_message(n = 0)
        return
    elif len(inputs) > 3:
        error_message(n = 2)
        return
    elif len(inputs) == 2 and inputs[1] == '-h':
        help_menu()
        return
    
    inputs = inputs[1:]
    validate_options = [True for char in inputs[0] if char in VALID_INPUTS]
        
    if sum(validate_options) != len(inputs[0]) - 1:
        error_message(n = 1)
        return

    else:
        print(inputs)
        print(gen_password(criteria = inputs[0].replace('-', ''), 
                            password_length = int(inputs[1])))

if __name__ == '__main__':
    main()