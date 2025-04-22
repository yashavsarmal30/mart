# ----- Single Inheritance -----
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# ----- Multiple Inheritance -----
class Father:
    def skills(self):
        print("Father: Gardening, Painting")

class Mother:
    def hobbies(self):
        print("Mother: Cooking, Dancing")

class Child(Father, Mother):
    def play(self):
        print("Child: Plays football")

# ----- Multilevel Inheritance -----
class Grandfather:
    def legacy(self):
        print("Grandfather: Family Values")

class Parent(Grandfather):
    def work(self):
        print("Parent: Engineer")

class Son(Parent):
    def dream(self):
        print("Son: Wants to be an artist")

# ----- Hierarchical Inheritance -----
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

# ------------------------------
# Output Section
# ------------------------------

print("----- Single Inheritance -----")
d = Dog()
d.sound()
d.bark()

print("\n----- Multiple Inheritance -----")
c = Child()
c.skills()
c.hobbies()
c.play()

print("\n----- Multilevel Inheritance -----")
s = Son()
s.legacy()
s.work()
s.dream()

print("\n----- Hierarchical Inheritance -----")
car = Car()
bike = Bike()

car.start()
car.wheels()

bike.start()
bike.wheels()
