import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
## RACE 1:
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.down() # 4. Pick up the pen so we don’t get lines
leonardo.down()
x = random.randrange(1,100)
leonardo.forward(x)
michelangelo.forward(x)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## RACE 2:
y = random.randrange(1,10)
z = random.randrange(1,10)
for i in range(10):
    leonardo.forward(y)
    michelangelo.forward(z)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)






# PART B - complete part B here-- I HAVE NO CLUE WHATS GOING ON
pygame.init()
window = pygame.display.set_mode()

screen_size = window.get_size()

side_length = 350
xpos = screen_size[0] / 2
ypos = screen_size[1] / 2

window.fill('deeppink3')
shapelist = [3, 4, 6, 20, 100, 360]
for num_sides in shapelist:
    points = []
    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x, y])
        ## surface, color, points, width
    pygame.draw.polygon(window, 'pink', points, 0)
    pygame.display.flip()
    pygame.time.wait(1800)
    window.fill('deeppink3')

## window.exitonclick()
