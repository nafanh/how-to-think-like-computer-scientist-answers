import turtle
import math
'''Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is 20 
units bigger, per side, than the one inside it. '''

def make_window(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w


def make_turtle(color, size):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t

def draw_square(t,sz):
    for i in range(4):
        t.left(90)
        t.forward(sz)


wn = make_window("lightgreen","spiral square")
tess = make_turtle("hotpink",3)
size = 20
# tess.speed(10)

for i in range(5):
    draw_square(tess, size)
    tess.right(45)
    tess.penup()
    tess.forward(10 * math.sqrt(2))
    tess.pendown()
    tess.left(45)
    size+=20
tess.penup()
tess.forward(-size)
tess.pendown()
wn.mainloop()
