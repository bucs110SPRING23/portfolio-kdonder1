# vending machine

# print("welcome to the vending machine")
# code = input("Please enter a code: ")
# money = int(input("Give me money: "))

# # functions are always defined in global scope
# # scope - where the data/ algorithm is accessible
# def my_vending_machine():
# if code == "A":
#     if money >= 1:
#         print("You got a coke")
#     else:
#         print("You need more money")
# elif code == "B":
#     if money >= 1.5:
#         print("You got a water")
#     else:
#         print("You need more money")
# elif code == "C":
#     if money >= 2:
#         print("You got juice")
#     else:
#         print("You need more money")
# else:
#     print("invalid code")

# my_vending_machine()
# my_vending_machine()
# my_vending_machine()


# Single Responsibility Principle
# A function should do one thing

# a function should never be responsible for input

# can access variables in global scope
def find_max(x, y, z): # x = a, y = b, z = c
    max = x
    if y > max:
        max = b
    if z > max:
        max = c

    print(max)

for _ in range(3):
    print("Please enter 3 numbers")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))
    find_max(a, b, c)

# collision
# - two variables of the same name
# - can't have variables of the same name in the same scope

b = 5
b = "5"

def foo(var): # function scope: var = var{5}
    var += 1 # using the same name as a global variable is called shadowing (making it essentially inaccessible)
    print(var)

var = 5
foo(var)
print(var)

find_max()
find_max()
find_max()