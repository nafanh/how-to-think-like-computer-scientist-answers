import turtle

def make_screen(color,title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color,sz):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(sz)
    return t


def draw_spiral(t,sz):

    size = sz
    for i in range(50):
        t.forward(size)
        t.right(90)
        t.forward(size)
        t.right(90)

        size += 10

def draw_tilt_spiral(t,sz):
    size = sz
    for i in range(50):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90+2)

        size+=10

wn = make_screen("lightgreen","spiral")
tess = make_turtle("blue",2)
tess.speed(10)

#draw spiral
draw_spiral(tess,50)

#Draw titled spiral
draw_tilt_spiral(tess,30)

wn.mainloop()

