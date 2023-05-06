# Turtle Code
# import turtle

# sides = input("Please type the number of sides you want your shape to have: ")
# length = input("Enter the length you want the sides of your shape to be: ")

# pen = turtle.Turtle()
# pen.shape("turtle")
# pen.color("blue")

# window = turtle.Screen

# for i in range(int(sides)):
#     pen.forward(int(length))
#     pen.right(360/int(sides))

# turtle.exitonclick()




# Pygame
# framework- collections of modules that don't have driver code in them. A bunch of stuff to use, but not a program by itself

# ================
# TOP OF FILE
import pygame

pygame.init()
# sets everything up

screen = pygame.display.set_mode()
# can set to be (300,300). Left blank creates a full window
# screen: variable
# pygame: the module (library) we are using.
# frameworks: modules that contain modules
# display: submodule of pygame
# set_mode: function of the display submodule

screen.fill("red")
pygame.time.wait(1000)
pygame.display.flip()
screen.fill("pink")
pygame.time.wait(1000)
pygame.display.flip()
screen.fill("green")
pygame.time.wait(1000)
pygame.display.flip()

screen_size = screen.get_size()

# [x, y, width, height]
dimensions = [screen_size[0] / 2, screen_size[1] / 2, 250, 250]
pygame.draw.rect(screen, "pink", [100, 100, 500, 500])

# [x, y, width, height]
dimensions = [500, 500, 250, 250]
pygame.draw.rect(screen, "blue", [200, 200, 500, 500])

pygame.display.flip()
pygame.time.wait(5000)