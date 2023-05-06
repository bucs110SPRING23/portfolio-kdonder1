# managing complexity - advanced programming just manages complexity
# Unix - 10,000 SLOC (source lines of code)
# Chrome - 10,000,000 SLOC
# OS X - 100,000,000 SLOC

# complex objects
# - primitives: int, str, float, lists, dict, tuple
# - turtle: x(int), y, heading, color(color), pensize(int), shape(string)
# my turtle : "x: 0, y: 0, heading: 0, color: (0,0,0), pensize: 1, shape: ('turtle')"

# bundle data and functions together
# - state: the current values of the data
# - behaviour: the functions that operate on the data in the object

# Point
# - object should do one thing
# state: x, y, color
# behaviour: change_color, move
# Classes == Type
import turtle

t= turtle.Turtle()
print(type(turtle.Turtle())) #complex
print(type(1)) #primitive

# classes are blueprints for objects
# - functions are stored algorithms
# - class as a stored data type
# classes are not executable
# don't put executable code in global scope, definitions are fine

# Point class
# - instance: an object created from a specific class
# - t = turtle.Turtle() # t is an instance of turtle
# - instance variable: a variable that is part of an instance
#   - t.x, t.pos # x and pos are instance variables
# - interface: the functions and variables of an object
#   - t.forward() # .forward() part of the interface if turtle

# Point - make it a class ourselves


### point.py
# def make_point(x, y):
class Point:
    # user types always start with a capital letter
    # - usually, classes go in their own file
    # - 1 class per file
    # dunders = double underscores on both sides of the name
    # addressing self.var ties the scope of var to the object scope

    def __init__(self): # self is the instance being created
        self.x = 0 # dot operator accesses instance variables of object
        self.y = 0
        self.color = ""


### main.py
import point
point.Point()

p1 = point.Point() # p1 is an instance of Point, Point is a class
p1.x = 10

p2 = point.Point()
p2.x = 5

# state of p1(x=10, y=0, color=""),
# state of p2(x=5, y=0, color="")

p1.color = "red"
# state of p1(x=10, y=0, color="red")
