# CREATING PARENT CLASS "MAMMAL"
class Mammal:
    def walk(self):
        print("Walking")


# CREATING CHILD CLASS "DOG" OF PARENT CLASS "MAMMAL"
class Dog(Mammal):
    def bark(self):
        print("Barking")


# CREATING CHILD CLASS "DOG" OF PARENT CLASS "MAMMAL"
class Cat(Mammal):
    def Meow(self):
        print("Meowing")


dog1 = Dog()  # Creating Object of Dog Class
dog1.bark()
dog1.walk()

print('')
print('')

cat1 = Cat()
cat1.Meow()
cat1.walk()
