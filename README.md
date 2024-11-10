# Number Guessing Game

Welcome to the **Number Guessing Game**! This is a simple Python-based game where the player has to guess a randomly generated number between 1 and 100. The game features two difficulty levels: **Easy** and **Hard**.

## Features:
- Choose between **easy** or **hard** difficulty levels.
- The game provides feedback after each guess: 
  - **Too high**
  - **Too low**
  - **You got it!**
- The player has a limited number of turns (attempts) to guess the correct number.
- If the player runs out of turns or guesses correctly, the game ends.

## How to Play:
1. **Choose a difficulty level**: Type `easy` for 10 attempts or `hard` for 5 attempts.
2. **Make a guess**: Enter a number between 1 and 100.
3. **Receive feedback**: The game will tell you if your guess was too high, too low, or correct.
4. **Keep guessing** until you either run out of attempts or guess the correct number!

## Game Flow:
- The game starts by welcoming the player and explaining the rules.
- It then generates a random number between 1 and 100.
- Based on the chosen difficulty, the player is given a set number of attempts to guess the number.
- After each guess, the number of remaining attempts is displayed, and feedback is provided.
- The game ends when the player guesses correctly or runs out of attempts.

## Installation:
To run this game, ensure you have Python installed on your computer. You can download Python from [python.org](https://www.python.org/downloads/).

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/number-guessing-game.git
## Example:
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
You have 9 attempts remaining to guess the number.
Make a guess: 30
Too low.
You have 8 attempts remaining to guess the number.
Make a guess: 40
You got it! The answer was 40.
