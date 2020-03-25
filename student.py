from Day_6 import Person

class student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    def enjoy(self):
        return ('Are you enjoying yourself {}?'.format(self.firstname))

    def talk(self):
        return ('I am chilling')

student_1 = student('Andy', 'Wakefield')

print(student_1.talk())
