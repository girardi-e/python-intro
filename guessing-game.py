import random

print(("*" * 30) + " GUESS THE SECRET NUMBER " + ("*" * 30))
print("")

# generate random number between 1 and 10
secret_number = random.randint(1, 10)

# keep track of user's guesses
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:

    # ask user to choose a number
    guess = int(input("Enter a number between 1 and 10: "))
    guess_count += 1

    # check if user made the right guess
    if guess == secret_number:
        print("*" * 50)
        print("CONGRATS! You've guessed the right number!")
        print("*" * 50)
    else:
        if guess_count < guess_limit:
            print("Wrong number!")
            print("Try again!")

print("")
print("Sorry! You've run out of guesses.")
print("")
print(f"The secret number was: {secret_number}")
