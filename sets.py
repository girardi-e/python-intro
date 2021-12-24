# A set is an UNORDERED Collection with NO DUPLICATE elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection,
# difference, and symmetric difference.

# create an empty set
empty_set = set()

students = {"Mike", "Mia", "Jenny", "Kevin", "Mia"}
# Mia is not printed twice
print(students)

# fast checking
print("Susan" in students)

# check length
print(len(students))

# adding, removing and updating
students.add("Dennis")
students.discard("Jenny")
students.update({"Chris", "Amanda"})
print(students)

# set operations
new_students = {"Luke", "Desiree", "Jamal", "Mike"}

# union
# students.union(new_students)
print(students | new_students)

# intersection
print(students & new_students)

# difference
print(students ^ new_students)






