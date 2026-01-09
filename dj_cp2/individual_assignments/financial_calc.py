#DJ, 1st, Financial Calculator
import os


def clear_screen():
    if os.name == 'nt': os.system('CLS')
    else: os.system('clear')

#define function, com_int_calc():
def com_int_calc():
    #starting_amount = user input: starting amount
    starting_amount = input("Starting Amount: ")
    #interest_rate = user input: interest rate percent
    interest_rate = int(input("Interest Rate Percent: "))
    #(interest_rate / 100) + interest rate = interest rate
    interest_rate += interest_rate / 100
    #years_compound = user input: years spent compunding
    years_compound = int(input("Years Spent Compounding: "))
    #final amount = 0
    final_amount = 0   

    #for year in years_compound:
    for year in range(years_compound):
        #starting_amount * interest rate + final amount
        final_amount += starting_amount * interest_rate

    #print At the end ot {years_compound} you will have {final amount}
    print(f"At the end of {years_compound} years, you will have ${final_amount}")
    return

#loop
while True:

    #Input menu containing the options for the calculator:
    option_one = input("1.) Compound Interest Calculator\n2.) Budget Allocater\n3.) Sale Price Calculator\n4.) Tip Calculator\n5.) Saving\n")
    #1.) Compound interest calculator
    #2.) Budget Allocater
    #3.) Sale Price Calculator
    #4.) Tip Calculator
    #5.) Saving

    #if input is equal to 1
    if option_one == "1":
        clear_screen()
        #Open compound interest calculator
        com_int_calc()
        clear_screen
        #restart loop
        continue

    #else if input is equal to 2
        #open buget allocater
        #restart loop

    #else if input is equal to 3
        #open sale price calculator
        #restart loop

    #else if input is equal to 4
        #open tip calculator
        #restart loop

    #else is input is equal to 5
        #open savings calulator
        #restart loop

    #else
        #ask user to enter valid input
        #restart loop
