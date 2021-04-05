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
def draw_square(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
wn = make_screen('lightgreen','pretty pattern')
tess = make_turtle('blue',2)
tess.speed(10)
for i in range(20):
    draw_square(tess,100)
    tess.penup()
    tess.left(360/20)
    tess.pendown()
wn.mainloop()