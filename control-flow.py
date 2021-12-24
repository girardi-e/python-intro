# if statement get executed only if its condition is True

number = int(input("Enter an integer: "))

if number < 0:
    number = 0
    print("Negative changed to zero")
elif number == 0:
    print("Zero")
elif number == 1:
    print("Single")
else:
    print("More")


# if statements and functions
def modify_name(name):
    if len(name) > 5:
        return name.upper()
    else:
        return name.lower()


new_name = modify_name("Luke")
print(new_name)


# nested if statements
def num_info(num):
    if num > 0:
        print("Greater than zero")
        if num > 10:
            print("Also greater than ten")


num_info(3)

