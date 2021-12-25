# In order to prevent our program from exiting when there is an error,
# we need to catch the Exception with a try except block.

try:
    num = int("a")
    print(num)
    # catch the exception and store it in a variable
except ValueError as e:
    print(f"Something went wrong! Message: {e}")

print("Exception was caught and reached end of program")
