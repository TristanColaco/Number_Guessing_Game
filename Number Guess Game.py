print("Welcome to the number guessing game!!!")

# The computer will generate a random integer between 1 and 100.
# You have to guess the correct number in the least amount of tries
# The computer will prompt if you number is higher or lower to the generated number

import random as rand
number = rand.randint(0, 100)

guess_counter = 0
game = True

while game == True:
    user_guess = int(input("Guess the whole number between 1 and 100: "))
    if user_guess < number:
        print("Number is higher!")
        guess_counter += 1
    elif user_guess > number:
        print("Number is lower")
        guess_counter += 1
    else:
        game = False


print(f"Hurray! You guess it within {guess_counter + 1} times!!!")