# Number Guessing Game

## Description

This is a simple command-line Number Guessing Game written in Python. The player chooses a difficulty level and attempts to guess a randomly generated number within a limited number of attempts.

After each guess, the program provides feedback indicating whether the guess was too high or too low. At the end of each game, the player can choose to play again or exit.

---

## Features

- Three difficulty levels:
  - **Easy:** Guess a number between **1 and 100**.
  - **Medium:** Guess a number between **1 and 500**.
  - **Hard:** Guess a number between **1 and 1000**.
- Limited number of attempts based on the selected difficulty.
- Input validation for menu selections and guesses.
- Feedback after every guess.
- Option to replay the game without restarting the program.

---

## Difficulty Levels

| Level | Number Range | Attempts |
| :--- | :---: | :---: |
| Easy | 1–100 | 7 |
| Medium | 1–500 | 11 |
| Hard | 1–1000 | 15 |

---

## Requirements

- Python 3.x

No external libraries are required. The program only uses Python's built-in `random` module.

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git
