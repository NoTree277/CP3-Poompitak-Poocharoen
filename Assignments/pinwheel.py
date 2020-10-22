import turtle
import random


def pinwheel(num_branch, size, backup):
    for n in range(num_branch):
        turtle.penup()
        turtle.pendown()
        turtle.forward(size)
        turtle.backward(backup)
        turtle.left(360 / num_branch)
        turtle.penup()


def random_pinwheel():
    for i in range(10):
        turtle.color(clr_list[random.randint(0, 7)])
        turtle.pensize(random.randint(3, 10))
        pinwheel(random.randint(4, 12), random.randint(30, 200), random.randint(25, 40))
        turtle.goto(random.randint(-300, 300), random.randint(-300, 300))


clr_list = ["red", "blue", "gold", "brown", "violet", "pink", "orange", "yellow"]
turtle.speed(10)
random_pinwheel()
turtle.done()
