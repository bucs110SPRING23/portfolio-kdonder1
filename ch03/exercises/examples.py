# bool - boolean value
# True/False
# - caps are important
# True, 1, "Hello"

print(type(True))

print(bool(1), bool(-1), bool("hello"))

print(bool(0), bool(" "), bool([]))
print()

# boolean expressions

x = 5
y = 10

print(x == y) # equality, == , booliean equality test,  = is assignmemnt
# boolean = returns either a single true or single false
print (x > y)
print(x < y)
print(x >= y) # => - NO
print(x <= y) # =< - ERROR
print( )

# and, or, not -semantic operators
# and: and == True, when x and why are both true

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print( )

# or - at least one True

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

# not - negation [!]

print(not True) # false
print("apple" == "apple")
print("apple" == "Apple Pie")
print("apple" < "Apple Pie")
print(ord("a"), ord("A"))
print( )

print(1 is int)
print(1 is 1)
print(1 is 5 // 5)
print( )

mynums = [1, 2, 3, 4, 5, 6, 7]
print(1 in mynums)
print(10 in mynums)
print( )

print(1 == 1.0)
print(1 is 1.0) # false- 1 is an int and 1.0 is a float
print(1 is 5 / 5) # makes float, CAN'T be compared
print(1 is 5 // 5) # makes int, can be compared
print( )

# a = int(input("num:"))

# if a < 0: # colon
#     a = abs(a) #indentation
# else: # no condition, always optional
#     print("positive")

# print(a) # de-indentation to end the if statement
# print( )

# a = int(input("num: "))
# if a > 5:
#     if a > 10
#         print(x is greater than 10)
#     else:
#     if a > 5
#         print("x is greater than 5")
#     if a > 10:
#         print("x is greater than 10")
# else:
#     print("x is less than or equal to 5")

# elif
# always goes between the if and else
# is optional
# can have as many as you like

# a = int(input("num: "))
# if a > 10: # need to put most selective condition first- "if"
#     print("x is greater than 10") 
# elif a > 5:
#     print("x is greater than 5") 
# else:
#     print("x is less than or equal to 5")

# if <boolean condition>: #required
#   # do something
# elif <boolean condition>: # optional
#   # do something
# else: # optional
#   # do something

### Fizzbuzz
# - loop through a range of values supplied by the user
# - for each value in the range
# - if the value is divisible by 3, print "fizz"
# - if the value is divisible by 5, print "buzz"
# - if the value is divisible by 3 and 5, print "fizzbuzz"

num = int(input("Insert an upper limit: "))
for i in range(num + 1):
    print("number: ", i )
    # if not i % 3
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        # else: error
        print("buzz")
