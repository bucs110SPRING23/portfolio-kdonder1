import random
import pygame

class LED:
    """
    docstring for Point
    """
    ## blueprint for an object
    ## def graph_point():
    ## class == type
    ## class are named with TitleCase
    ## turtle.Turtle, module.Class

    # functions are called 'methods" when they're in a class
    # first parameter of any method is 'self'
    def __init__(self, x=0, y=0, color="red"):
        # self ties the data to the objects scope
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), 5, 5)
        self.color = color
        self.radius = 5
        # no return

    def random_color(self):
        colors = ["red", "green", "blue", "yellow", "orange", "purple"]
        self.color = random.choice(colors)



    # import point
    # import sub.module
    # from sub.module import module
    # from Rectangle import rectangle






## MVC: Module View Controller
# for GUI programs
# accumulator pattern
# Design Patterns - language independent

# View - dispalys things on screen
#      - pygame
#      - turtle

# Controller: controls things on screen
#    - keyboard

#   - Model
#   - a class
#   - contains the data for the prorams
#   -
