from tkinter import *

tk=Tk()
canvas=Canvas(tk ,width=500,height=500)
canvas.pack()

canvas.create_rectangle(100,100,200,200,fill="blue")