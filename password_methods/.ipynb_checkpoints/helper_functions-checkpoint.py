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