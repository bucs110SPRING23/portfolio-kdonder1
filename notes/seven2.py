import LED
import random
import turtle
import pygame

pygame.init()
display = pygame.display.set_mode()

point = []
for p in range(10):
    x = random.randint(0, 250)
    y = random.randomint(0, 250)
    p = point.Point(x, y)
    p.random_color()
    points.append(p)

p1 = point.LED(x=100, y=100)

while True:
    pygame.display.flip()

pygame.draw.circle(display, p1.color, (p1.x, p1.rect.y), p1.radius)
pygame.display.flip()

# print(p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1))
# p2  =point.Point(3, 4, "yellow")
# print(p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2))

# points = []
# for p in range(10):
#     x = random.randint(0, 100)
#     y = random.randint(0, 100)
#     points.append(point.Point("orange"))

# t = turtle.Turtle()
# for p in points:
#     t.color(p.color)
#     t.goto(p.xcoor, p.ycoor)

# turtle.Screen().exitonclick()

# def changecolor = [random.randinto(),"green"]
# new_color = random.randint(0, 255)
    
    



# main

#cases
# - snakecase: snake_case, underscores for spaces, all lowercase
# - camelcase: camelCase, capital for spaces, starts lowercase lowercase
# - TitleCase: Titlecase, capital for spaces, starts lowercase