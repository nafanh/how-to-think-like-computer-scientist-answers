import turtle

def make_screen(color,title):
    wn = turtle.Screen()
    wn.bgcolor(color)
    wn.title(title)
    return wn

def make_turtle(color,sz):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(sz)
    return t

wn = make_screen("lightgreen","drunken pirate")
tess = make_turtle("blue",3)
pairs = [(90,50),(-45,25*(2**0.5)),(-90,25*(2**0.5)),(-45,50),
         (-90,50),(-135,50*(2**0.5)), (135,50),(135,50*(2**0.5))]
for angle,steps in pairs:
    tess.left(angle)
    tess.forward(steps)
tess.hideturtle()
wn.mainloop()