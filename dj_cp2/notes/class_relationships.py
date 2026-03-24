#DJ, 1st, Class Relationships Notes

#What is polymorphism?
    # Many Shapes
    # A method that does many different things

#What is inheritance?
    # A child function taking in the parent functions

#What do we call the classes in an inheritance relationship?
    # Parent and Child

#How does inheritance simplify your code?
    # Easier to read
    # Makes a base
    # Less repeating

#What is aggregation? 
    # Only works one way
    # Relationship is "has is"

#How do you use aggregation?
    # Look at something that is being repeated and make it its own class

#How does aggregation simplify your code?
    # Easier to read
    # More detailed
    # More modular
    # Shorter

#What is composition?
    # Compisition means one class cannot exist without another

#How do you use composition?
    # Like aggregation but it needs another class to exist

#How does composition simplify your code?
    # Easier to read
    # More detailed
    # More modular
    # Shorter



# INHERITANCE / POLYMORPHISM


# Parent Class
class Vehical:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
    
    def move(self):
        print("Move")


# Child Class
class Car(Vehical):
    pass

class Boat(Vehical):
    def move(self):
        print("Sail")

class Plane(Vehical):
    def move(self):
        print("Fly!")


boat = Boat("Touring 20", "Ibiza")
car = Car("750S Spider", "McLaren")
plane = Plane("Boeing", "747")


print(car.brand)
print(car.model)
car.move()
boat.move()
plane.move()


# AGGREGATION


class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog

    
    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)

        else:
            print("This book isn't in this library.")
    
    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title.title()
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    

lib = Library("Provo Library")

lib.add_book(Book("Way Of Kings", "Brandon Sanderson"))
lib.add_book(Book("Fellowship of the Ring", "J. R. R. Tolkein"))
lib.add_book(Book("The Last Battle", "C. S. Lewis"))

lib.view_catalog()