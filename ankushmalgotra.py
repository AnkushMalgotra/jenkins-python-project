import random
import time

# Simple number guessing game
def number_guess_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Welcome to Ankush's Number Guessing Game!")
    print("I have picked a number between 1 and 10. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guess_game()
