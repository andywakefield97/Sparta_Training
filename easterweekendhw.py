#Key examples of Python coding learnt at Sparta
#Includes if, loops, methods and functions, classes, examples of OOP, using excel files.

import xlsxwriter

#Classes used as a blueprint for the Apples
class Apple:
# INIT method to intialise the class and tell it which variables to run first
    def __init__(self, category, weight, age):

#Variables defined within the method
        self.category = category
        self.age = age
        self.weight = weight

# IF, ELIF AND ELSE Functions used within a method.
    def weight_category(self):
        if self.weight >= 500:
            return "Large"
        elif self.weight >= 250:
            return "Medium"
        else:
            return "Small"

    def age_category(self):
        if self.age >= 10:
            return "Class 3"
        elif self.age >= 6:
            return "Class 2"
        else:
            return "Class 1"

# Example of FOR looping used to return each letter from category of apple variable.
#Use of '__' before the method name encapsulates (Pillar of OOP) making it uncallable outside of the class
    def __category_loop(self):
        for x in self.category:
            if x == 'C':
                continue
            return x
#Example of a While loop that returns weight when over 100g
    def acceptance_weight(self):
        w = self.weight
        while w >100:
            return "Weight of {}g is acceptable".format(w)
        else:
            return "Weight of {}g is lower than 100g and therefore not acceptable".format(w)
            


class ExcelOutput(Apple):
    #Example of Inheritance (Pillar of OOP) using the super() keyword.
    def __init__(self, category, weight, age, worksheet):
        super().__init__(self, category, weight, age)

    #Example of using xlsxwriter to create excel files
    def excel_creator(self, name):
        spreadsheet = xlsxwriter.Workbook("{}.xlsx".format(name))
        worksheet = spreadsheet.add_worksheet("Apples")

    #Example of appending and editing pre-existing excel files
    def excel_writer(self, worksheet):
        worksheet.write("A1", self.category)
        worksheet.write("B1", self.weight)
        worksheet.write("C1", self.age)
        worksheet.close()



#defining a variable
apple1 = Apple("Braeburn", 300, 4)
apple2 = Apple("Cox", 105, 10)

if __name__ == '__main__':
    print(apple1.weight_category())
    print(apple2.acceptance_weight())



#Note on lists, tuples, dicts and sets not used in program:
List = [2,4,6,7,8,4]
Tuple = (9,6,53,34,8)
Dictionary = {"Pasta": 56, "Rice": 67, "Potato": 89}
Set = {"Pasta", "Rice", "Brocolli"}
    