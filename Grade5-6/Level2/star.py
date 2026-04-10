import turtle 

t=turtle.Turtle()
# def draw_star(size,point):
#     for i in range (point):
   
#         t.forward(100)
#         if i%2==0:
#             t.left(size)
#         else:
#             t.left(size)

# draw_star(20,15)
# turtle.done()


def draw_star(size,point):
    for i in range (1,19):
        t.forward(point)
        if i%2==0:
            t.left(size)
        else:
            t.left(225)
    def draw_star():
     t.color(0.8,0.3,0.4)
     t.begin_fill()
     t.circle(100)
     t.end_fill()
draw_star(175,100)
turtle.done()