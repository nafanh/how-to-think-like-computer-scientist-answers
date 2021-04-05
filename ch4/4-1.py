import turtle
'''Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image shown below. Assume 
each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square 
when the program ends.) '''

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


def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = make_window("lightgreen", "multiple squares")
tess = make_turtle("hotpink", 3)
tess.speed(10)
for i in range(5):
    draw_square(tess, 20)
    tess.penup()
    tess.forward(40)
    tess.pendown()
wn.mainloop()
