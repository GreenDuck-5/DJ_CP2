#DJ, 1st, Update Personal Library
import csv

def show(library):
    pass

def add(saved, library):
    return saved, library

def update(saved, library):
    return saved, library

def delete(saved, library):
    return saved, library

def save(saved, library):
    
    with open("dj_cp2/individual_assignments/animals.csv", mode="w", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=["Animal", "Scientific Name", "Classification", "Average Length (m)", "Average Height (m)"])
        writer.writeheader()
        writer.writerows(library)
    
    saved = True
    print("Library saved.")
    
    return saved

def load():

    library = []

    with open("dj_cp2/individual_assignments/animals.csv", mode="r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            item = {"animal": row.get("Animal", "").strip(), "scientific_name": row.get("Scientific Name", "").strip(), "calssification": row.get("Classification", "").strip(), "average_length": row.get("Average Length (m)", "").strip(), "average_height": row.get("Average Height (m)", "").strip()}
            
            library.append(item)

    return library

def main():

    saved = False
    library = []
    library = load()

    while True:
        print("""Personal Library:\n1. Show list\n2. Add item\n3. Update item\n4. Delete item\n5. Save library\n6. Reload library from fil\n7. Exit""")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show(library)
        elif choice == "2":
            saved, library = add(saved, library)
        elif choice == "3":
            saved, library = update(saved, library)
        elif choice == "4":
            saved, library = delete(saved, library)
        elif choice == "5":
            saved = save(saved, library)
        elif choice == "6":
            library = load()
            print("Reloaded library")
        elif choice == "7":
            quit()
        else:
            print("Invalid option. Please enter a number from 1 to 7.")

main()