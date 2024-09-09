import turtle
#turtle.speed("fastest")

turtle.fillcolor("orange")
turtle.pencolor("blue")

#draw a square
sides = 4
i = 0
turtle.begin_fill()
while i < sides:
    turtle.forward(100)
    turtle.right(90)
    i = i + 1
turtle.end_fill()

#draw a triangle
turtle.goto(150,150)
sides = 3
i = 0
turtle.begin_fill()
while i < sides:
    turtle.forward(100)
    turtle.right(120)
    i = i + 1
turtle.end_fill()

input()