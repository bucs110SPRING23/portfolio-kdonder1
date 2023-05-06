import random

number = random.randrange(11)

for _ in range(3):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Correct!")
        break
    elif guess > number:
        print("Too High!, Guess again!")
    else:
        print("Too Low! Guess again!")
