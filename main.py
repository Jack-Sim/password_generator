#!/usr/bin/env python3 

import sys
from password_methods.methods import *
from password_methods.helper_functions  import *

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
    print("hello")
    main()