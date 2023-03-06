import random

# for loop - a set number of iterations
#    iterating over a collection
# while - more control over the loop

number = random.randrange(1001)
print(number)
guesscount = 0

while True:
    num = 0
    guess = int(input("Guess a number between 1 and 1000: "))
    if guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        guesscount += 1
        print("Correct!, you guessed in", guesscount, "tries!")
        break
    guesscount += 1
    print(guesscount)


# number = random.randrange(1001)
# print(number)

# msg = "Enter a number between 1 and 5: "
# number = int(input(msg))
# while number > 5 or num < 1:
#         num = int(input(msg))

# print("Done!")

# While Loop
# 'While <boolean condition>: 
    # <code block>
# if boolean condition is True, execute the code block
    # otherwise, skip it


# for i in range(10):
#     print(i)

# i = 0 #iterating variable
# while i < 10:
#     print(i)
#     i += 1 #iterating variable must change

# mylist = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
# i = 0 #iterating variable
# while i < len(mylist):
#     print(mylist[i])
#     i += 1 #iterating variable must change


# for i in range(10):
#     print(i)
#     i += 3

# # while loop maintains the state of the iterating variable

# i = 0
# while i < 10:
#     print(i)
#     i += 3 #iterating variable must change

# # any for loop can be recreated with a while loop
# # some while loops cannot be recreated with for loops

# print("Enter numbers to sum ['q' to quit]")
# sum = 0
# while True
#     value = input("number: ")
#     if value.isdigit():
#         value = int(value)
#         sum += value # sum = sum + value
#     elif value == 'q':
#         break
# print("Your number is: ", sum)


# i = 0
# while i < 5:
#     if random.randrange(2):
#         i += 1
#     print(i)