import tkinter as tk
import os
window = tk.Tk()
window.title("My First GUI")
window.geometry("600x600")

label = tk.Label(window, text="Welcome to Tkinter!")

button_x = 250 # Starting x position

def move_button():
    global button_x
    button_x += 50  # Move right by 50 pixels
    if button_x > 500:  # If it goes too far right, wrap back to the left
        button_x = 50
    button.place(x=button_x, y=500)
    label.config(text="Button Moved!")

button = tk.Button(window, text="Click Me", command=move_button)

# Build the absolute path to the image in the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "leen.png")

img = tk.PhotoImage(file=img_path)

# Scale down the image (e.g., by a factor of 2). Increase the numbers to make it even smaller!
img = img.subsample(5, 5)

image_label = tk.Label(window, image=img)

image_label.pack()
button.place(x=button_x, y=500) # Use .place() instead of .pack()
label.pack()
window.mainloop()