import turtle

# User inputs:
sides = input("Please type how many sides you want your shape to have: ")
length = input("How long do you want the sides of your shape to be: ")
sides = int(sides)
length = float(length)

# determining the angles in the shape:
angle = 360/sides

# Turtle:
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)
pen.color("pink")
window = turtle.Screen()

# repetition
for i in range(sides):
    pen.forward(length)
    pen.right(angle)

turtle.exitonclick()