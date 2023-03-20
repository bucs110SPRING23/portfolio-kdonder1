import turtle

# initialize
PEN = turtle.Turtle()
PEN2 = turtle.Turtle()
WINDOW = turtle.Screen()
YMAX = 300
XMAX = 400
## XMAX and YMAX are the dimensions of the screen


value = 1
value2 = 0

# drawing
def motion(xcor, ycor):
    ## this function draws the lines. This is the repeating pattern that appears on the screen.
    ## checks the parameters, xcor and ycor, to ensure that the lines are only being drawn within the screen
    ## this function does not return any variables 
    if ycor > -YMAX - 20 and xcor < XMAX + 20:
        onWINDOW(xcor, ycor)
        PEN.forward(50)
        PEN.color("red")
        PEN.right(60)
        PEN.forward(50)
        PEN.color("darkblue")
        PEN.left(60)


# is the turtle in the WINDOW?
def onWINDOW(xcor, ycor):
    ## this function sets where the turtle goes when it reaches the bottom or rightmost side of the screen, then picks up the PEN and resets the turtles position.
    ## this function uses the parameters xcor and ycor, which are the the components of the turtles position when turtle is moved from the bottom of the screen to it's next initial position.
    ## the parameters, xcor and ycor, are returned when the function is completed.
    global value
    global value2
    print("xcor: ", xcor)
    print("ycor: ", ycor)
    print("current value :", value)
    if ycor <= YMAX:
        ycor = -YMAX + value * 50
        xcor = -XMAX
    else:
        ycor = YMAX + 25
        xcor = -(XMAX + 45) + value2 * 90
    # PEN getting picked up
    if PEN.xcor() > XMAX:
        print("JUMP____________________________________________________")
        value = value + 1
        PEN.up()
        PEN.goto(xcor, ycor)
        PEN.down()
        if ycor >= YMAX:
            value2 = value2 + 1
            print("VALUE 2", value2)
        return value, value2
    elif PEN.ycor() < -YMAX - 10:
        print("JUMP____________________________________________________")
        value = value + 1
        PEN.up()
        PEN.goto(xcor, ycor)
        PEN.down()
        return()
    return xcor, ycor, value, value2

def circle(circlex, circley):
    # turtle.circle(radius, extent=None, steps=None)
    PEN2.up()
    PEN2.begin_fill()
    PEN2.goto((circlex,circley))
    PEN2.circle(50, None, 360)
    PEN2.end_fill()
    PEN2.down()
    return circlex, circley 

# main code
def main():
    PEN.shape("turtle")
    PEN.speed(0)
    PEN.color("darkblue")
    PEN2.shape("turtle")
    PEN2.speed(0)
    PEN2.color("yellow")
    # initialize position
    PEN.up()
    PEN.goto(-XMAX, -YMAX)
    PEN.down()
    xcor = 0
    ycor = 0
    circlex = 100
    circley = 100
    for i in range(2):
        circlex, circley = circle(-circlex, -circley)
    PEN2.up()
    for i in range(200):
        motion(xcor, ycor)
main()