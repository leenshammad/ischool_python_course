
import turtle


t = turtle.Turtle()


for _ in range(4):
    print(_)
    t.forward(100)
    t.penup()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.pendown()

turtle.done()