import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    guess_count = 0
    guess_limit = 10

    while guess != number_to_guess:
        if guess_count < guess_limit:
            guess = int(input("Guess a number between 1 and 100: "))
            guess_count += 1
            if guess < number_to_guess:
                print("Too low!")
                if number_to_guess - guess <= 10:
                    print("You're almost there! \n")
            elif guess > number_to_guess:
                print("Too high!")
                if guess - number_to_guess <= 10:
                    print("You're almost there!")
            if guess != number_to_guess and guess_count < guess_limit:
                print(f"You have {guess_limit - guess_count} guesses left.\n")
        else:
            print("Sorry, you've reached the maximum number of guesses. Better luck next time!")
            return
    print("Congratulations! You guessed the number.")

guess_the_number()
