def add_two_numbers(x, y):
    return x + y


num_one = 45
num_two = 56

print(add_two_numbers(num_one, num_two))


# pass an argument with a default value to a function
def greeting(name, greeting="Hello"):
    print(f"{greeting}, {name}.")


greeting("Emilio")
greeting("Bob", "Hola")


def create_query(language="Javascript", num_stars=50, sort="desc"):
    return f"language: {language}, number of stars: {num_stars}, sorting order: {sort}"


my_query = create_query("Python")
print(my_query)


# Don't do this
def foo(a, b=[]):
    b.append(a)
    print(f"B is: {b}")


foo(7)
foo(4)


# Do this!
def bar(a, b=None):
    if b is None:
        b = []
        b.append(a)
        print(b)
