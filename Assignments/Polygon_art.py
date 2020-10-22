import turtle
import random

turtle.speed(10)
turtle.setheading(0)


def polygon(x, y, size, n, clr):
    turtle.penup()
    turtle.color(clr)
    turtle.fillcolor(clr)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(size)
        turtle.left(360 / n)
    turtle.end_fill()


polygon_num = 1
while polygon_num <= random.randint(20, 30):
    polygon(random.randint(-300, 300), random.randint(-300, 300), random.randint(20, 100), random.randint(3, 8), "blue")
    polygon_num += 1

turtle.done()
