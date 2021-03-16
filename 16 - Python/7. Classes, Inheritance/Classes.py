# ------------------------------------------------------
# We always have to give a default paramter "self" while
# working wooth function inside of a class
# ------------------------------------------------------

class MyClass():
    def someFunction(self):
        print("I just ran a function inside of a class")

    def anotherFunction(self):
        print("2nd function ran inside of a class")


a = MyClass()  # Created Object of class MyClass & stored it to variable 'a'

a.someFunction()
a.anotherFunction()
