import turtle
#turtle.speed("fastest")

turtle.fillcolor("orange")
turtle.pencolor("blue")
sides = 4
i = 0
turtle.begin_fill()
while i < sides:
    turtle.forward(100)
    turtle.right(90)
    i = i + 1
turtle.end_fill()
input()