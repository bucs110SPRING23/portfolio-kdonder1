import turtle
import random

def is_in_screen(w, t):
    return True

t = turtle.Turtle()
t.shape("turtle")
t.speed(4)

wn = turtle.Screen()
wn.bgcolor("black")

distance = 30
angle = 90
# is_in_screen = True

colors = ["red", "green", "blue", "yellow", "orange"]

while is_in_screen(wn, t):
    coin = random.randrange(0,2)
    if coin == 0: # heads
        t.right(angle)
    else: # tails
        t.left(angle)
    t.forward(distance)

    turtleX = t.xcor()
    turtleY = t.ycor()
    # x, y = t.pos()

    x_range = wn.window_width() / 2
    y_range = wn.window_height() / 2

    t.color(random.choice(colors))

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False

wn.exitonclick()
