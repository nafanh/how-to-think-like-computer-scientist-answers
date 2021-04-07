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
data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
for angle,steps in data:
    tess.left(angle)
    tess.forward(steps)

wn.mainloop()