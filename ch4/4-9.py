import turtle

def make_window(color,title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color,size):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t
def draw_star(t,sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)
wn = make_window('lightgreen','star')
tess = make_turtle('black',3)
draw_star(tess,100)
tess.hideturtle()
wn.mainloop()
