import turtle

t=turtle.Turtle()
def draw_oxtgon():
    for i in range (8):
        t.forward(100)
        t.left(45)

def draw_circle():
    t.color(0.8,0.3,0.4)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def draw_star():
    for i in range (1,19):
        t.forward(100)
        if i%2==0:
            t.left(175)
        else:
            t.left(225)


draw_oxtgon()
draw_star()
draw_circle()

turtle.done()

