# DJ, 1st, Student Creator
import csv

class Student_Maker:


    def __init__(self, name, id, grade, academicstanding):
        self.name = name
        self.id = id
        self.grade = grade
        self.academicstanding = academicstanding


    def __str__(self, name, id, grade, academicstanding):
        print(f"""Name: {name}
ID: {id}
Grade: {grade}
Academic Standing: {academicstanding}
""")


    def save_data(self, name, id, grade, academicstanding):
        with open('individual_assignments/grade book/docs/students.csv', mode = 'w+', newline ='') as file:
            writer = csv.writer(file)

            writer.writerows(name, id, grade, academicstanding)
    

name = input("")
id = input("")
grade = input("")
academicstanding = input("")


student = Student_Maker(name, id, grade, academicstanding)


print(student)