import turtle
import random

# collection objects
# strings - list characters - immutable (items can't be changed)
# lists - list of any set of objects - mutable (items can be changed)
# tuples - immutable list of any set of objects
mytuple = (5, 8, 123456789, 5)
# mytyple[0] = 1 # ERROR!
# dictionaries - use to store key/value pairs
mydictionary = { "a":1, "b":2, "c":3}
mydictionary["a"] = turtle.Turtle()
mydictionary["d"] = 4


number = random.randrange(101)
print(number)

for _ in range(101):
    guesscount = []
    print(guesscount)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > number:
        print("Too High!")
        guesscount.append(guesscount + 1)
    elif guess < number:
        print("Too Low!")
        guesscount.append(guesscount + 1)
    else:
        print("Correct!, you guess in ", guesscount, "tries!")