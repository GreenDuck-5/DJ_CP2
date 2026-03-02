#DJ, 1st, Personal Library

#dicitonary with the animals: animals
animals = {
    "Mallard": "Anas Platyrhynchos",
}

#clear the screen
def clear_screen(): print("\033c", end = "")

#Let user pick when to move on
def continue_screen(): input("Press \"Enter\" or \"Return\" to continue:\n")

#add function
def add():
    #clear_screen()
    clear_screen()
    #common_name = user input: what is the common name
    common_name = input("What is the common name?\n").title()
    #scientific_name = user input: what is the scientific mname
    scientific_name = input("What is the scientific name?\n").title()
    #print: common name: common_name
    print(f"Common name: {common_name}\nScientific name: {scientific_name}")
    #print: scientific name: scientific_name
    #add common name and scientific name together to the dicitonary
    animals[common_name] = scientific_name
    #continue_screen()
    continue_screen()
    #return
    return

#view function
def view():
    #clear_screen()
    clear_screen()
    #for animal, animalz in animals
    for animal, animalz in animals.items():
        #print: Common name: animal
        print(f"{animal} A.K.A. {animalz}")
        #print: Scientific name: animalz
    #continue_screen
    continue_screen()
    #return
    return

#search function
def search():
    #loop
    while True:
        #clear_screen()
        clear_screen()
        #how_search = user input: common name or scienftofca name
        how_search = input("Common Name or Scientific Name?:\n").lower()
        #search = search:
        search = input("Search: ").lower()
        #fi how search = "common nmae"
        if how_search == "common name":
            #for key in animals
            for animal in animals.keys():
                #if key = search
                if animal.lower() == search:
                    #print: key
                    print(f"{animal}")
                    # input = remove thsis animal?, y/n
                    remove = input("Remove this animal? Y/N:\n").strip().lower()
                    # if input = y
                    if remove == "y":
                        #remove search
                        del animals[animal]
                    continue_screen()
                    return
        #if how search = "scientific name"
        elif how_search == "scientific name":
            #for animal, animalz in animals
            for animalz, animal in animals.items():
                #if animalz = search
                if animal.lower() == search:
                    #print: animalz
                    print(animal)
                    # input = remove thsis animal?, y/n
                    remove = input("Remove this animal? Y/N:\n").strip().lower()
                    # if input = y
                    if remove == "y":
                        #remove search
                        del animals[animalz]
                    continue_screen
                    return
        else:
            print("Please enter valid input")
            continue_screen()
            continue

#irtorduction()
def introduction():
    #introduce the user
    print("This is the place where you can store all your animals. Why? I have no idea. But you can. Add them by common name then scientific name.")
    continue_screen()

#main function
def main():
    while True:
        #clear_screen
        clear_screen()
        #give options of what to do: add, search, remove, view, introduce, exit
        to_do = input("Add, search, remove, view, introduce, exit:\n").lower().strip()

        #list options to do
        options_to_do = ("add", "search", "remove", "view", "introduce", "exit")
        
        #if the user picks "add":
        if to_do == "add":
            # add()
            add()
            # return
            return

        #if the user picks "view"
        elif to_do == "view":
            # view()
            view()
            # return
            return

        #if the user picks "search"
        elif to_do == "search":
            # search()
            search()
            # return
            return

        #if the user picks "remove"
        elif to_do == "remove":
            print("Search for what you want to remove")
            continue_screen()
            # search()
            search()
            # return
            return

        #if the user picks "introduce"
        elif to_do == "introduce":
            #introduction()
            introduction()
            #return
            return

        #if the user picks "exit"
        elif to_do == "exit":
            #exit()
            exit()

        else:
            print("Please enter valid input")
            continue_screen()
            continue

#introduction()
introduction()
#loop
while True:
    #main_function
    main()