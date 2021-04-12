import turtle
'''
Write a void function draw_equitriangle(t, sz) which calls draw_poly from the previous question to have its turtle draw a equilateral triangle.

'''
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

wn = make_window("lightgreen",'octagon')
tess = make_turtle("hotpink","3")

def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

def draw_equitriangle(t,sz):
    draw_poly(t,3,sz)

draw_equitriangle(tess,50)

wn.mainloop()