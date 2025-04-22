

text = "  Hello, Python Programming!  "

print("Original string:", repr(text))


print("Stripped:", text.strip())


print("Lowercase:", text.lower())
print("Uppercase:", text.upper())


print("Index of 'Python':", text.find("Python"))
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

words = text.strip().split()
print("Split into words:", words)

joined_text = "-".join(words)
print("Joined with '-':", joined_text)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet 1:", set1)
print("Set 2:", set2)


set1.add(7)
print("Set1 after adding 7:", set1)

set1.remove(2)
print("Set1 after removing 2:", set1)


print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))


print("Length of set1:", len(set1))
print("Is 5 in set1?", 5 in set1)
