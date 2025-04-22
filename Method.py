# ----- Method Overloading -----
class Calculator:
    def add(self, a, b=0, c=0):  # Default arguments to simulate overloading
        return a + b + c

# Creating a Calculator object
calc = Calculator()

print("Add 2 numbers:", calc.add(10, 20))     # Method Overloading (2 arguments)
print("Add 3 numbers:", calc.add(10, 20, 30)) # Method Overloading (3 arguments)


# ----- Method Overriding -----
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # Overriding the parent class method
        print("Dog barks")

class Cat(Animal):
    def speak(self):  # Overriding the parent class method
        print("Cat meows")

# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()

print("\n----- Method Overriding -----")
dog.speak()  # Calls overridden method in Dog class
cat.speak()  # Calls overridden method in Cat class
