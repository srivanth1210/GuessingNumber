from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()  # Convert input to lowercase
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid choice. Please choose 'easy' or 'hard'.")

def get_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

turns = set_difficulty()  # Set the number of turns based on the chosen difficulty
print(f"You have {turns} attempts remaining to guess the number.")

# Game loop
while turns > 0:
    guess = get_guess()  # Get a valid guess
    check_answer(guess, answer)
    turns -= 1
    if guess == answer:
        break
    elif turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
    else:
        print(f"You've run out of turns. The game is over! The correct answer was {answer}.")
