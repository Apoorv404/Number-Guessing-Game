from art import logo
from random import randint

number = randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    life = 10
elif difficulty == 'hard':
    life = 5
else:
    raise SystemExit("Invalid difficulty level")


game_over = False


while not game_over:
    print(f"You have {life} attempts to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        game_over = True
        print(f"You got it right! It was {number}")
    elif guess < number:
        life -= 1
        print("Too low!")
    elif guess > number:
        life -= 1
        print("Too high!")

    if life == 0:
        game_over = True
        print(f"You've ran out of guesses. It was {number}. You lose.")
