# Write a python program to implement Abstract class, Abstract
# method and Interfaces in Python.

from abc import ABC, abstractmethod

# ----- Abstract Class and Abstract Method -----
class Animal(ABC):  # Animal class is abstract because it inherits from ABC
    @abstractmethod
    def speak(self):  # Abstract method (no implementation)
        pass

class Dog(Animal):
    def speak(self):  # Dog class provides the implementation of the abstract method
        print("Dog barks")

class Cat(Animal):
    def speak(self):  # Cat class provides the implementation of the abstract method
        print("Cat meows")

# ----- Interface Simulation Using Abstract Base Class -----
class Shape(ABC):  # Shape class acts as an interface
    @abstractmethod
    def area(self):  # Abstract method to calculate area
        pass
    
    @abstractmethod
    def perimeter(self):  # Abstract method to calculate perimeter
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# ----- Using the Abstract Class and Interface -----
# Creating instances of Dog and Cat
dog = Dog()
dog.speak()  # Dog's implementation of the abstract method

cat = Cat()
cat.speak()  # Cat's implementation of the abstract method

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("\n----- Shape Interface -----")
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
