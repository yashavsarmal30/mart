# Write a python program to implement Basic data types

name = input("Enter Your name:- ")
age = int(input("Enter your age:- "))
height = float(input("Enter your height:- "))
is_student = input("Enter yes for student otherwise no:- ")
is_student = is_student.lower() == 'yes'

subjects = ['Maths', 'Science', 'Language']
dob = (2004, 1, 21)
hobbies = {"reading", "travelling", "Gaming"}

student_info = {
    "name": name,
    "age": age,
    "height": height
}

next_year_age = age + 1
height_in_cm = height * 100
is_adult = age > 18
eligible_for_discount = is_student or is_adult

print("\n--- Output ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Your age next year:", next_year_age)
print("Your height in cm:", height_in_cm)
print("Are you an adult?", is_adult)
print("Subjects (List):", subjects)
print("Date of Birth (Tuple):", dob)
print("Hobbies (Set):", hobbies)
print("Student Info (Dictionary):", student_info)
print("Eligible for Discount:", eligible_for_discount)
