#DJ, 1st, Classes Notes


#What is a class in python?
    # A blueprint for objects

#What is an object in python?
    # One instance of your class

#How do python classes relate to python objects?
    # Python classes are the outline for objects and create them

#How do you create a python class?
    # see below

#What are methods?
    # functions specific to a class

#How do you create a python object?
    # using a class

#How to you call a method for an object?
    # class_name.function_name

#Why do we use python classes?
    # it cuts down the amount of code needed, and creates a base to easier create more code. it assists with code readability, and its more efficient


class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nspecies: {self.species}\nage: {self.age}\n"
    
    def birthday(self):
        self.age += 1


dog = Animal("Doug", "Dog", 4)
bunny = Animal("Judy", "Rabbit", 20)
print(dog)
print(bunny)
dog.birthday()
print(dog)


class ClassPeriod:
    def __init__(self, subject, teacher = "Ms. LaRose", room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}\n"
    
first = ClassPeriod("CP 2", room = 200)
second = ClassPeriod("CP 2", room = 200)
third = ClassPeriod("CSP", room = 200)
sixth = ClassPeriod("CSP", room = 200)
print(first, second, third, sixth)