#DJ, 1st, Random Password Generator

import random
import string


#function for clearing screen
def clear_screen(): print("\033c", end = "")

#function for letting user pick when to move on
def continue_screen(): input("Press \"Enter\" or \"Return\" to continue:\n")

#make a list with all the lowercase characters
def get_lowercase():
    return string.ascii_lowercase

#make a list with all the uppercase characters
def get_uppercase():
    return string.ascii_uppercase

#make a list with all the numbers
def get_numbers():
    return string.digits

#make a list with all the special characters
def get_special_characters():
    return string.punctuation


#take in the lengnth and what things hte user wants to make the password by into a function
def generate_password(length, char_pool):
    #password
    password = ""
    #loop through the lengeth og the password
    for i in range(length):
        #add a character from the list of choices og ythe user
        password += random.choice(char_pool)
    return password

#functiuon to generate all passwoerds
def generate_passwords():
    #ask user howaa long for the passsword
    while True:
        length = input("\nHow long does the password need to be: ")

        if length.isdigit():
            length = int(length)
            break

        else:
            print("Please enter vlaid input.")
            continue_screen()

    #if to use lower
    use_lower = input("Does the password need lowercase letters (Y/N): ").upper()
    #if to user upper
    use_upper = input("Does the password need uppercase letters (Y/N): ").upper()
    #if ot use numbers
    use_numbers = input("Does the password need numbers letters (Y/N): ").upper()
    #if to use special characters
    use_special = input("Does the password need special characters letters (Y/N): ").upper()

    clear_screen()

    #list witth all the thinfs the user can want
    char_pool = ""

    #add items to characre poolv ased off uesr choices
    if use_lower == "Y":
        char_pool += get_lowercase()
    if use_upper == "Y":
        char_pool += get_uppercase()
    if use_numbers == "Y":
        char_pool += get_numbers()
    if use_special == "Y":
        char_pool += get_special_characters()

    if char_pool == "":
        print("You must select at least one character type.")
        continue_screen()
        return

    print("Possible Passwords:")

    #generate four passworsd
    for i in range(4):
        print(generate_password(length, char_pool))
    
    print("\n")
    
    continue_screen()


#main funciton
def main():
    #welcome user
    print("Welcome to the Password Generator!")

    #loop
    while True:
        #ask user whta ot do
        print("Type the number for the action you would like to perform")
        print("1. Generate Passwords")
        print("2. Exit")

        choice = input("")

        #pick waht ot do based off user choices
        match choice:

            case "1":
                clear_screen()
                #generate passwoers
                generate_passwords()
                clear_screen()
            case "2":
                #exit
                print("\nThank you for using the Password Generator. Goodbye!")
                exit()
            case _:
                print("\nInvalid choice. Please select 1 or 2.")

#run main function
main()