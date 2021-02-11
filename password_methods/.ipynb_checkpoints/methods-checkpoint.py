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
