import random

# generate random number between 1 and 10
secret_number = random.randint(1, 10)

# keep track of user's guesses
number_of_guesses = 0

# ask user to choose a number
guess = input("Enter a number between 1 and 10: ")

print(("*" * 100) + "GUESS THE SECRET NUMBER" + ("*" * 100))
print("*" * 300)
# while number_of_guesses < 3 and guess != secret_number:

