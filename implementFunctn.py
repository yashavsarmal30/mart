# Write a python program to implement Functions

numbers = [10, 20, 30, 40, 50]
print("Built-in Function Example:")
print("Sum of numbers:", sum(numbers))  


def greet(name):
    return f"Hello, {name}."

print("\nUser-Defined:")
print(greet("YashAvsarmal"))



square = lambda x: x * x
add = lambda a, b: a + b

print("\nAnonymous Function (Lambda):")
print("Square of 6:", square(6))
print("Addition of 10 and 20:", add(10, 20))
