import turtle
import random

# Create the turtle
pen = turtle.Turtle()

def create_heart():
    # Move to starting position
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

def random_hex_color():
    """Generates a random hexadecimal color code string (e.g., '#AABBCC')."""
    # Generate a random integer between 0 and 0xFFFFFF (16777215)
    random_int = random.randint(0, 0xFFFFFF) 
    # Format it as a 6-digit hex string with leading zeros
    return f"#{random_int:06x}" 


for i in range(0,1):
    pen.color('red')
    create_heart()
# Keep the window open
turtle.done()