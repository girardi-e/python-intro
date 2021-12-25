from pprint import pprint

# Create an empty list
empty_list = []
another_empty_list = list()

# Create a new list with items
students = ["Karen", "Jill", "Mark", "Steve", "Monica"]
new_students = ["Jimmy", "Maggie"]
lucky_numbers = [3, 3, 7, 13, 33, 107]

# pretty print for long lists
pprint(students)
print(students[3])

# updating a list item
students[3] = "Sarah"

# slicing returns a new list
print(students[:2])

# create a list containing other lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][0])

# Methods

# length
print(len(students))

# adding and removing items
students.extend(new_students)
print(students)

lucky_numbers.append(16)
print(lucky_numbers)

# (position, item)
students.insert(1, "Kelly")
print(students)

lucky_numbers.remove(16)
print(lucky_numbers)

students.pop()
lucky_numbers.pop(4)
del students[3]
# students.clear()

# Look for an item
"Jimmy" in students
"Sarah" in lucky_numbers

print(students.index("Jimmy"))

# Count how many times an item appears in a list
print(lucky_numbers.count(3))

# Sort and reverse a list
# sorted(students)
students.sort()
print(students)

# sorted(lucky_numbers, reverse=True)
lucky_numbers.reverse()
print(lucky_numbers)

# copy  a list
print(students[:])

unlucky_numbers = lucky_numbers.copy()
print(unlucky_numbers)
