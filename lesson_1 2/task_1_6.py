# Create 2 modules: 1. containing data about student; 2. using data from first module
import students

print(students.name)
print(" Students name is {} surname is {} age {} curs {}".format(students.name, students.surname,
                                                           students.age, students.curs))
