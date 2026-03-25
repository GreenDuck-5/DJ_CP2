#DJ, 1st, Financial Calculator
import os
import time
      
#define function, com_int_calc():
def com_int_calc():
    #starting_amount = user input: starting amount
    starting_amount = int(input("Starting Amount: "))
    #interest_rate = user input: interest rate percent
    interest_rate = int(input("Interest Rate Percent: "))
    #years_compound = user input: years sepnt compounding
    years_compound = int(input("Years Spent Compounding: "))

    final_amount = starting_amount * ((1 + (interest_rate / 100)) ** years_compound)

    #print At the end ot {years_compound} you will have {final amount}
    print(f"At the end of {years_compound} years, you will have ${final_amount}")
    input("Press \"Enter\" or \"Return\" to continue:\n")
    return

#define function, budget allocater
def budget_all():
    #num_categories = user input: how many budget categories do you have
    num_categories = int(input("How many budget categories do you have: "))
    
    #nake empty lists for categories and percentages
    categories = []
    percentages = []

    #ask for categories name for each categorie number, staritng at one
    for i in range(1, num_categories + 1):
        #category = user inout: categort {i}:
        category = input(f"Category {i}: ")
        #appened categorie to lost
        categories.append(category)

    #income = user input: waht is you montyhluy ijncome
    income = float(input("What is your monthly income: "))

    #assign each category a name by user coice
    for category in categories:
        percent = float(input(f"What percent is your {category}: "))
        percentages.append(percent)

    #assign category to percent
    for category, percent in zip(categories, percentages):
        amount = income * percent / 100
        print(f"{category} is ${amount}")

    input("Press \"Enter\" or \"Return\" to continue:\n")
    return

#define function, sales price
def sale_price():
    #original_cost = user input: how much does the item originally cost
    original_cost = float(input("How much does this item originally cost?\n"))
    #discount_percent = user input: what percent is the discount
    discount_percent = float(input("What percent is the discount?\n"))
    #discount_perecemt /= 100
    discount_percent /= 100
    #final_price = original_cost * dicount_percent
    final_price = original_cost - (original_cost * discount_percent)
    #print: the tiem now costs {final_price}
    print(f"The item now costs ${final_price}")
    input("Press \"Enter\" or \"Return\" to continue:\n")
    return

#define function, tip calculator
def tip_calc():
    #bill-amount = user input: waht is the orginal bill
    bill_amount = float(input("What is the original bill amount?\n"))
    #tip_percent = useer inopt: whtaw os the tip amount
    tip_percent = float(input("What is the tip percentage?\n"))
    #tip_amount = equation
    tip_amount = float((tip_percent / 100) * bill_amount)
    #print: the tip amount is {tip-ampount} and teh final bill is {bill_amount + tip_amoint}
    print(f"The tip amount is ${tip_amount} and the final bill is ${bill_amount + tip_amount}")
    input("Press \"Enter\" or \"Return\" to continue:\n")
    return

#define function, saving
def saving_calc():
    #saving amount = user input: what amount are you saving ot
    saving_amount = input("What amount are you saving to?\n")
    #loop
    while True:
        #time contributing = user input: how often are you contributing
        time_contributing = input("How often are you contributing:\n1.) Weekly\n2.) Monthly\n")
        #1. Weekly
        #2. Monthly
        #if time_contrubuting = 1 or 2
        if time_contributing == "1" or time_contributing == "2":
            #break loop
            break
        #else
        else:
            #restart loop
            print("Please enter valid input")
            time.sleep(1)
            continue
    #amotung contributeds = user ijnput: how much are you contributing each time
    amount_contributing = input("How much are you contributing each time?\n")
    #if time_contributing = 1
    contributions_needed = saving_amount / amount_contributing
    if time_contributing == "1":
        #legnth to save ofr weekly contributions
        print(f"It will take {contributions_needed} weeks to reach your goal.")
    #else if time_contributing = 2
    if time_contributing == "2":
        #length to save for monthly contributions
        print(f"It will take {contributions_needed} months to reach your goal.")
    input("Press \"Enter\" or \"Return\" to continue:\n")
    return

#define function, menu
def menu():
    #loop:
    while True:
        #check what os the user is using, then clearing the screen based off that
        def clear_screen(): os.system('CLS') if os.name == 'nt' else os.system('clear')

        #Input menu containing the options for the calculator:
        option_one = input("1.) Compound Interest Calculator\n2.) Budget Allocater\n3.) Sale Price Calculator\n4.) Tip Calculator\n5.) Saving\n").strip()
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
            clear_screen()
            #restart loop
            continue

        #else if input is equal to 2
        elif option_one == "2":
            clear_screen()
            #open budget allocater
            budget_all()
            clear_screen()
            #restart loop
            continue

        #else if input is equal to 3
        elif option_one == "3":
            #open sale price calculator
            clear_screen()
            sale_price()
            clear_screen()
            #restart loop
            continue

        #else if input is equal to 4
        elif option_one == "4":
            clear_screen()
            tip_calc()
            #open tip calculator
            clear_screen()
            #restart loop
            continue

        #else is input is equal to 5
        elif option_one == "5":
            clear_screen()
            #open savings calulator
            saving_calc()
            clear_screen()
            #restart loop
            continue

        #else
        else:
            #ask user to enter valid input
            print("Please enter valid input.")
            time.sleep(1)
            #restart loop
            clear_screen()
            continue

menu()