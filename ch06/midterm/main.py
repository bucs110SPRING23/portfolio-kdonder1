import turtle

# initialize
PEN = turtle.Turtle()
WINDOW = turtle.Screen()
YMAX = 300
XMAX = 400
## XMAX and YMAX are the dimensions of the screen



# is the turtle in the WINDOW?
def onWINDOW(value, value2):
    ## this function sets where the turtle goes when it reaches the bottom or rightmost side of the screen, then picks up the PEN and resets the turtles position.
    ## this function uses the parameters value and value2, which reset the variables that determine where the turtle goes when it reaches the bottom of the screen.
    ## the parameters, value and value2, are returned when the function is completed.
    xcor = 0
    ycor = 0
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
    elif PEN.ycor() < -YMAX - 10:
        print("JUMP____________________________________________________")
        value = value + 1
        print("VALUE VALUE VALUE", value)
        PEN.up()
        PEN.goto(xcor, ycor)
        PEN.down()
    print(xcor, ycor, value, value2)
    return value, value2 



# main code
def main():
    PEN.shape("turtle")
    PEN.speed(0)
    PEN.color("darkblue")
    # initialize position
    PEN.up()
    PEN.goto(-XMAX, -YMAX)
    PEN.down()
    xcor = 0
    ycor = 0
    value = 1
    value2 = 0
    for i in range(200):
        if ycor > -YMAX - 20 and xcor < XMAX + 20:
            onWINDOW(value, value2)
            PEN.forward(50)
            PEN.color("red")
            PEN.right(60)
            PEN.forward(50)
            PEN.color("darkblue")
            PEN.left(60)
        print("range")
        value, value2 = onWINDOW(value, value2)
main()