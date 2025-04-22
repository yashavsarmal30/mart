
numbers = (10, 20, 30, 40, 20, 50)
fruits = ("apple", "banana", "cherry", "banana")


print("Numbers Tuple:", numbers)
print("First element in numbers:", numbers[0])
print("Last element in fruits:", fruits[-1])


print("\nLength of numbers tuple:", len(numbers))


print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

print("Sum of numbers:", sum(numbers))


print("Count of 20 in numbers:", numbers.count(20))
print("Count of 'banana' in fruits:", fruits.count("banana"))


print("Index of 30 in numbers:", numbers.index(30))
print("Index of 'cherry' in fruits:", fruits.index("cherry"))

combined = numbers + (60, 70)
print("\n Combined Tuple:", combined)
