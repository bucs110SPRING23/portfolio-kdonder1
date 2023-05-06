# # define a function
# def star_pyrimid(rows): # rows = levels
#     for i in range(rows): # range(5), range(1, 5), range(1, 5, 2)
#         print("*" * (i + 1))

# # define a function
# def rstar_pyrimid(rows):
#     for i in range(rows, 0, -1): # start, stop, step
#         print("*" * i)

# # scope
# levels = int(input("Enter the desired pyrimid height: "))

# star_pyrimid(levels)
# rstar_pyrimid(levels)



# def foo(x, y, z):
#     print(x, y, z)

# foo(1, 2, 3)
# foo(2, 1, 3)
# foo(3, 2) # ERROR - not enough parameters

# def bar(x=0, y=2, z=3):
#     print(x, y, z)

# bar(1, 2) # z got set to a default value- have more flexibility
# bar(z=1, x=2)


# local variables get deleted at the end of the funciton
# parameters are local variables
# def foo():
#     local_var = 5 # local scope
#     x = 2 # deleted when this ends

# def foo():
#     local_var = 5
#     print(x)

# global_var = 5



# def my_min(x,y,z):
#     result = x # local scope
#     if result > y:
#         result = y
#     if result > z:
#         result = z
#     print("in my_min:", result)

# result = 0
# my_min(1,2,3)
# print(result)

# f(x) = y
# functions must return a value

# def foo():
#     x = 5
#     # return None: NoneType

# def bar (x=None):
#     if x is None:
#         x = 5

# print(foo())

# def foo():
#     x = 5
#     if x > 5:
#         return x
#     else:
#         return 5
#     return [x, 4] # never executed

# y, x = foo()
# print(y)
# print(foo())

# def my_func(x = 0):
#     return x + x # scope to my_func

# my_func(5)
# print(x)


# def powerof(x=0, p=0):
#     power = p + power # local scope = makes the global variable inaccessible
#     y = x ** power
#     return y

# # y = f(x)
# power = 2
# result = powerof(5, 3)
# print(result)


# def foo():
#     x = 5
#     print(x*x) # no return statement... printing a value - noop

# def foo2():
#     x = 5
#     return x*x # returning a value

# print(foo()) # nested functions exectue from the inside out
# print(foo2())



# def fooBar():
#     x = 5
#     y = 6
#     return x * y



# 100000000 line program
# name collisions
# glboal variables never leave memory while the program is running
var = 5

def start():
    print(var)
    return True

def dosomething():
    print(5)
    

# x = 5
# start(x)

def main(): # main functions
    x = 5
    start(x)
    dosomething()

main() # call the main function in global scope