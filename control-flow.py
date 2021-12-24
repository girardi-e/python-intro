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
