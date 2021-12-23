# Tuples are IMMUTABLE, and usually contain a HETEROGENEOUS sequence of
# elements that are accessed via unpacking or indexing

# creating an empty tuple
empty_tuple = ()

# creating a tuple with a single item
one_item_tuple = (1,)

# creating a tuple with multiple items: with our without ()
student = ("Marcy", 17, [18, 8, 1985], "History", 3.5)
# student = "Marcy", 17, [18, 8, 1985], "History", 3.5
print(student[0])

# unpacking a tuple
name, age, birthdate, subject, gpa = student
# name, age, birthdate, subject, _ = student
print(subject)

# searching for an item
print("Sarah" in student)


# return a tuple from a function
def http_status_code():
    return 200, "OK"


print(http_status_code())

code, name = http_status_code()
print(code)
