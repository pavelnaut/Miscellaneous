import sys
 
 
class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.second_name = last_name
 
 
class Teacher(Human):
    def __init__(self, first_name, last_name, intelligence, competence):
        Human.__init__(self, first_name, last_name)
        self.intelligence = intelligence
        self.competence = competence
 
 
class DreamTeacher(Teacher):
    def __init__(self, first_name, last_name, intelligence, competence, empathy, charm):
        Teacher.__init__(self, first_name, last_name, intelligence, competence)
        self.empathy = empathy
        self.charm = charm
 
    def __str__(self):
        return f"Thank you for..."
        # TODO
 
 
my_teacher = DreamTeacher('Ines', 'Ivanova', sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize )
 
try:
    print(my_teacher)
except:
    print(f"Stop kidding me. There is no way to raise exception in this case!")
