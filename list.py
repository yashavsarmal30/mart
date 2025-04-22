# Write a python program to implement Different List and List Operations

fruits=["apple","banana","cherry"]
numbers=[10,20,30,40,50]
mixed=["Aniket",21,True,5.6]
nested=[[1,2],[3,4],[5,6]]
print("Fruits List:", fruits)
print("Numbers List:", numbers)
print("Mixed List:", mixed)
print("Nested List:", nested)

print(fruits[0])
print("First two numbers:-",numbers[0:2])
fruits.append("orange")
print("After appending Orange",fruits)
numbers.insert(2,25)
print("After inserting numbers",numbers)
fruits.remove("banana")
print("After Removing Banana",fruits)
popped_item = numbers.pop()
print("Popped item is:-",popped_item)
print("After popping item:-",numbers)
fruits.reverse()
print("After reversing",fruits)
print("Length of mixed list",len(mixed))