# **L1: Solving on loops**

**Loop 🔁:** A loop is like a magic spell that makes your computer repeat things automatically! It saves us from typing the same code over and over again.

```python
fruit_list = ["Orange", "Banana", "Strawberry"]
for fruit in fruit_list:
    print(fruit)
```

**range() function 📏:** It tells the computer exactly how many times to repeat the magic loop.

* 1,2,3,4,5 : range(1,6) # stops right before 6!  
* 1,3,5,7 : range(1,8,2) # start, end, and skip by 2  
* 7,8,9 : range(7,10)  
* 0,1,2 : range(3)

```python
for i in range(1,6):
    print(i)        # will print the numbers 1 to 5
```

**Control statements 🚦:** Special words like break (stop!), continue (skip this one!), and pass (do nothing right now) help us control the loop like a traffic light.

```python
i = 0
while True:
    i = i+1
    if i > 5 :
        break # STOP the loop!

for i in range(1,5):
    if i == 3:
        continue # SKIP the number 3!
    print(i)     # prints 1, 2, 4

def draw_star():
    pass # DO NOTHING yet
```

**Nested loop 🪆:** Just like Russian nesting dolls, you can put one loop completely inside another one!

```python
count = 0
for i in range(8):
    for j in range(3):
        print(count)
        count += 1
```

# **L2: Function In Python**

**Function 🛠️:** A function is like a recipe! You write it once, give it a name, and use it whenever you want the computer to do that specific chore.

```python
def say_hello():
    print("Welcome to the lesson!")
```

**Calling a function: 📣:** This just means saying the function's name out loud in the code so the computer runs your recipe!

```python
say_hello()
```

# **L3: Python Modules**

**Module 📦:** A module is like a toy box full of extra tools that other smart people wrote. You can open the box and use the tools in your own code!

```python
import my_tools
my_tools.do_something()
```

**Math module 🧮:** A box full of cool math tricks!

```python
import math

number = math.sqrt(25)
print(number)  # Output: 5.0
```

**Datetime module ⏱️:** A box that helps the computer know exactly what time and day it is right now.

```python
import datetime

current_time = datetime.datetime.now()
print(current_time)
```

**Module documentation 📖:** This is a built-in guide that tells you how to use a tool box.

```python
import math
help(math)
```

# **L4: Solving on Function and Modules**

**Module 📦:** Remember, this is a file with ready-to-use code!

**Function 🛠️:** A named block of code that does one special job to keep our program tidy.

```python
import math

result = math.sqrt(16)
print(result) # Output: 4.0

def greet_user(name):
    print("Hello, " + name + "!")

greet_user("Mohamed")
```

# **L5: Classes and Objects**

**Class 🗺️:** A class is like a blueprint or a cookie cutter. It tells the computer how to build something, like a robot!

```python
class Robot:
    pass # Empty blueprint
```

**Object 🤖:** If the class is the cookie cutter, the object is the actual cookie! It's the real robot we created.

```python
my_robot = Robot()
```

**Attribute 🎨:** Something that describes the object, like its paint color or its name.

```python
class Robot:
    def __init__(self):
        self.color = "blue" # Attribute
```

**Method 🏃‍♀️:** An action the object can do, like jumping or speaking!

```python
class Robot:
    def jump(self): # Method
        print("Robot is jumping!")
```

**init function ⚙️:** A special step that happens first to set up our object with its name and color when it's born.

```python
class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model
```

# **L6: Following Classes**

**Inheritance 👨‍👧:** When a new object (like a Drone) gets all the cool abilities of its parent (like a base Robot). It inherits them!

```python
class BaseRobot:
    def move(self):
        print("Moving forward")

class DroneRobot(BaseRobot): # Inherits from BaseRobot!
    def fly(self):
        print("Taking off")

drone = DroneRobot()
drone.move() # It can move just like its parent!
```

**Function Overriding 🦸‍♀️:** When the child object changes how it does something to be unique! Like instead of saying "Beep", it says "Whirrrrr".

```python
class BaseRobot:
    def speak(self):
        print("Beep")

class DroneRobot(BaseRobot):
    def speak(self): # Changing the parent's action!
        print("Whirrrrr")
```

# **L7: Solving on Classes**

**Class 🗺️**, **Object 🤖**, **Inheritance 👨‍👧**, and **Function Overriding 🦸‍♀️**:

Let's put all these puzzle pieces together! We can create a Car object from a Vehicle blueprint, and make it drive.

```python
class Vehicle:
    def __init__(self, speed):
        self.speed = speed
          
    def show_speed(self):
        print(f"Speed: {self.speed}")

class Car(Vehicle): # Inheritance
    def show_speed(self): # Overriding
        print(f"Car is driving at {self.speed} km/h")

my_car = Car(120)   
my_car.show_speed()
```

# **L8: Built-In Functions**

**Built-in Function 🎁:** Special tools Python gives us for free from the very beginning. We don't even need to open a box to use them!

```python
name_length = len("SiNova") # Counts the letters!
highest_score = max(85, 92, 78) # Finds the biggest number!
print(highest_score)
```

**Handling Files in Python 📝:** How to make the computer open a text file, read the words inside, write new words, and close it when done.

```python
# Writing to a file
file = open("data.txt", "w")
file.write("Saving some important data.")
file.close()

# Reading from a file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

# **L9: Turtle Graphic**

**Turtle Module in Python 🐢:** A super fun drawing tool where a little virtual turtle moves around the screen and draws lines wherever it goes!

```python
import turtle

t = turtle.Turtle()
t.forward(100) # Move turtle forward
t.right(90)    # Turn turtle right by 90 degrees
```

**.pen() in Python Turtle: 🖌️:** You can change the turtle's pen to draw in different colors, make lines thicker, or move faster!

```python
import turtle

t = turtle.Turtle()
t.pen(pencolor="blue", pensize=5, speed=10)
t.forward(50)
```

# **L10: More Turtle Graphics**

**Drawing with Loops 🔁🐢:** We can use loops to tell the turtle to repeat steps, making shapes like squares easily!

```python
import turtle

t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
```

**Drawing Circles in Turtle ⭕:** A quick trick to make the turtle draw a perfect round circle.

```python
import turtle

t = turtle.Turtle()
t.circle(50) # Draws a circle!
```

# L11: Tkinter in Python

### Tkinter 🪟
A fun tool to build your very own app windows with buttons and text!

```python
import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.geometry("300x200")

label = tk.Label(window, text="Welcome to Tkinter!")
label.pack()

window.mainloop()
```

**Displaying Images 📸:** How to put a nice picture file inside your app window.

```python
import tkinter as tk

window = tk.Tk()
img = tk.PhotoImage(file="logo.png")   
image_label = tk.Label(window, image=img)
image_label.pack()
window.mainloop()
```

**Creating Basic Animation 🎬:** Making things move around inside your app!

```python
# General concept for animation:
# canvas.move(item, x_change, y_change)
# window.after(delay_ms, update_function)
```
