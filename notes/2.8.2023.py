# here are my notes for today! We're going to see how this note-taking method goes lol
import math
import turtle

#simulate pen and paper: see justforfun.py

#for loop

# for <iterating_variable> in <sequence, 0, 0, 0>
    #this sequence will loop 4 times

#     #do something with iterating variable
# msg = "Enter 3 numbers"
# mynums = []
# for i in [0,0,0]:
#     var = int(input(": "))
#     mynums.append(var)
#     print(mynums)
# print("all done")

# block statement
    #always ends with colon

#there is repetition in this code:
    # mynums = []
    # var = int(input("Enter a number: "))
    # mynums.append(var)
    # print(mynums)
    # var = int(input("Enter another number"))
    # mynums.append(var)
    # print(mynums)
    # var = int(input(": "))
    # mynums.append(var)
    # print(mynums)


colors = ["red","orange", "yellow", "green", "blue", "purple"]
for c in colors:
    print(c)
    c = "black"
    print(c)
print(colors)

for ch in "hello":
    print(ch)



#for using a list WHY ISNT THIS WORKING PLEASE
# mylist = [] * 5
# for i in mylist:
#     print("Happy Birthday")

## range()
'range(5)' == [0, 1, 2, 3, 4] #python said I had to use two equals signs here.... why????
#range generates list values dynamically
# [0]*100 generates a list of 100 0's and stores it in memory!
# 'range(100) # generates items from a list of 100 as needed

result = range(5) #starts at 0 (default), stops at 5 (non-inclusive)
print(list(result))
result = range(1, 5) # starts at 0, stops at 5 (non-inclusive)
print(list(result))
result = range(1, 20, 2) #starts at 1 (inclusive), stops at 20 (non-inclusive), steps by 2
print(list(result))

print(list(range(11)))
print(list(range(3, 10, 2)))

# range(stop)
# range(start, stop)
# range(start, stop, step)
# goes up to, but doesn't include, the stop

# print(list(range(100, -1, -1)))
# my list = list(range(1, 11))
# print(list(range(len(mylist))))


for _ in range(5):
    print("Happy Birthday")


for _ in range(4):
    #insert code you want to repeat
# gets rid of iteration

# colors = ["red", "purple"]  ## are able to add as many colors as I want in this line without having to add other stuff
# for color in colors:
#     donatello.color(color)

#can put for loops inside of forloops

#programming- abstracting out a solution that is able to solve more problems than just the original problem

# can use any python packages that you want to use
    # put it into requirements file
    # we will use pygame