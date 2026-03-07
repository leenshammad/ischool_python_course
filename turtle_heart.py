import turtle

# Create the turtle
pen = turtle.Turtle()
pen.color("red")
# Move to starting position
pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# Keep the window open
turtle.done()