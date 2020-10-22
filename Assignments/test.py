"""import turtle
turtle.speed(10)
turtle.setheading(0)

turtle.penup()
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(200, -100)
turtle.seth(360)
turtle.pendown()
turtle.begin_fill()
turtle.fd(600)
turtle.seth(-90)
turtle.fd(60)
turtle.seth(180)
turtle.fd(600)
turtle.seth(90)
turtle.fd(60)
turtle.end_fill()

turtle.penup()
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(460, 0)
turtle.seth(270)
turtle.pendown()
turtle.begin_fill()
turtle.fd(260)
turtle.seth(0)
turtle.fd(60)
turtle.seth(90)
turtle.fd(260)
turtle.seth(180)
turtle.fd(60)
turtle.end_fill()

turtle.done()"""

a = int(input("Enter the terms"))
f = 0  # first element of series
s = 1  # second element of series
if a <= 0:
    print("The requested series is", f)
else:
    print(f, s, end=" ")
    for x in range(2, a):
        next = f + s
        print(next, end=" ")
        f = s
        s = next
