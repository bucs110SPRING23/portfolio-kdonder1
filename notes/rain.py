## Controller = like a model, label for how a class is used

# Model - data
# View - display (pygame)
# Controller - Logic (director)
    """
    file: main.py
    """

import pygame
import point

from src.controller import Controller


def main():
    controller = Controller()
    controller.mainloop()


# self.graph.points.draw()
    # draws itself

main()


# in def __init(self):
    # INITIALIZE
# organize code into dunders to make it easier to follow
    # allows us to keep state

# minimize the amount of pygame stuff we have in our models
# Sprites - anything that moves around the screen, anything that interacts with something else on the screen
# inheritance



class Foo():
    def __init__(self):
        self.num = 5

    def addone(self):
        self.num += 1

class Bar():
    def __init(self):
        self.num = 5
    
    def addone(self):
        self.num += 1

Class Bar(Foo):
    def adsub(self):
        self.num += 1

b = Bar()

b.addone()
b.addsub()


# self.image - instance variable, must be a Surface object
# hook method