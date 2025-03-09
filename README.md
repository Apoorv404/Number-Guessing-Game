# Number-Guessing-Game

A Python-based number guessing game where players try to guess a randomly generated number between 1 and 100 within a limited number of attempts.

## Python Concepts Implemented

- **Random Number Generation**: Using `randint()` from the `random` module
- **Control Flow**: Using while loops and if-else statements
- **User Input Handling**: Taking and validating user input
- **Type Conversion**: Converting string input to integers
- **Error Handling**: Handling invalid difficulty level input
- **Game State Management**: Tracking lives and game over conditions
- **String Formatting**: Using f-strings for output

## Features

- Two difficulty levels:
  - Easy: 10 attempts
  - Hard: 5 attempts
- Feedback on each guess (too high/too low)
- Remaining attempts counter
- ASCII art game logo
- Input validation

## Files

- [`main.py`](main.py): Core game logic
- [`art.py`](art.py): ASCII art logo
- `README.md`: Documentation
- `LICENSE`: MIT license

## How to Play

1. Run the `main.py` script
2. Choose difficulty level ('easy' or 'hard')
3. Guess a number between 1 and 100
4. Get feedback on your guess (too high/too low)
5. Keep guessing until you find the number or run out of attempts

## Example Game

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts to guess the number.
Make a guess: 50
Too high!
You have 9 attempts to guess the number.
Make a guess: 25
Too low!
...
```
