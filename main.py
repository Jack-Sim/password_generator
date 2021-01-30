#!/usr/bin/env python3 

import sys
import random

VALID_INPUTS = ['l', 'u', 'n', 's']

char_options = {'l': 'abcdefghijklmnopqrstuvwxyz',
                'u': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                'n': '1234567890',
                's': '`¬!"£$%^&*()-=+\{\}[];:@\'#/.>,<\|?~'}

def gen_password(criteria = 'l', password_length = 10):

    """
    gen_password is a function to create a password with the
    criteria and the length specified.

        parameters:
            criteria (str): 
                A string with the groups of characters that should be 
                included in the password
            password_length (int): 
                Desired password length

        Returns:
            password (str): 
                The randomly generated password 
    """

    password = ''
    for i in range(password_length):
        character_pick = criteria[random.randrange(len(criteria))]
        password += random.choice(char_options[character_pick])
    
    valid_password = validate_password(password, criteria)

    return valid_password

def validate_password(password, criteria):

    """
    validate_password will check the password created and ensure it meets 
    the specified criteria. If the password does not meet all criteria, 
    the gen_password function is rerun. If the password passes the validation
    then the password is returned.

        parameters:
            password (str): 
                The generated password to be validated
            criteria (str): 
                A string with the groups of characters that should be 
                included in the password

        Returns:
            password (str): 
                The validated password, once the checks have been passed 
    """
    
    is_valid = []
    
    for crit in criteria:
        check_for_char = [True for c in password if c in char_options[crit]]
        if sum(check_for_char) > 0:
            is_valid.append(True)
        else:
            is_valid.append(False)
    
    if sum(is_valid) == len(criteria):
        return password
    else:
        return gen_password(criteria, len(password))

    

def error_message(n=0):
    """
    A function to print the desired error messages to the console
    The input n determines the error to be displayed
        Parameters:
            n (int):
                The number of the error to be displayed
    """
    if n == 0:
        print("[ERROR] - Not enough arguments, please refer to help menu using -h")
    elif n == 1:
        print("[ERROR] - Invalid options, please refer to help menu using -h")
    elif n == 2:
        print("[ERROR] - Too many parameters, please refer to help menu using -h")

def help_menu():
    """
    Function to print the help menu to the console.
    """
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
        print(gen_password(criteria = inputs[0].replace('-', ''), 
                            password_length = int(inputs[1])))

if __name__ == '__main__':
    main()