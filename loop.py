# Write a python program to implement Looping in Python (while loop, for loop, nested loop)

print("While loop:-Print sum of squares of first 15 natural numbers")
sum_squares=0
num=1
while num<=15:
	sum_squares+=num**2
	num+=1
print("Sum is",sum_squares)

print("For loop:-Print each character of word Python")
for ch in "Python":
	print(ch,end='\n')
print("\n")

print("Nested loop:- Printing a 3x3 matrix of *")
for i in range(3):
	for j in range(3):
		print("*",end=' ')
	print()
	
