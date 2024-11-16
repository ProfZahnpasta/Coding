import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Turtle Game")
screen.bgcolor("white")

t = turtle.Turtle()
zoom_factor = 1

def zoom_in():
    global zoom_factor
    zoom_factor *= 1.1

def zoom_out():
    global zoom_factor
    zoom_factor /= 1.1

def mouse_wheel(event):
    if event.delta > 0:
        zoom_in()
    else:
        zoom_out()

screen.getcanvas().bind("<MouseWheel>", mouse_wheel)

while True:
    randomn = random.randint(1,4)
    if randomn == 1:
        t.forward(100 * zoom_factor)
    if randomn == 2:
        t.left(90)
    if randomn == 3:
        t.backward(100 * zoom_factor)
    if randomn == 4:
        t.right(90)
    randomg = random.randint(1,10)
    t.pensize(randomg)
    screen.update()
    
screen.mainloop()