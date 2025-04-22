# Python Program to demonstrate Classes, Objects, Constructors, Static Methods, and Inner Classes

class Student:
    # Constructor
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # Instance method
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

    # Static method
    @staticmethod
    def welcome_message():
        print("Welcome to the Student Management System!")

    # Inner Class
    class Address:
        def __init__(self, city, pincode):
            self.city = city
            self.pincode = pincode

        def show_address(self):
            print(f"City: {self.city}, Pincode: {self.pincode}")

# ----- Using the Class -----
# Calling the static method without creating an object
Student.welcome_message()

# Creating a Student object
s1 = Student("Aniket", 101)
s1.display()

# Creating an object of the Inner class
address = Student.Address("Mumbai", 400001)
address.show_address()
