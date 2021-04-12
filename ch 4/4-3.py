import turtle
'''
Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon. When called with draw_poly(tess, 8, 50), it will draw a shape like this:
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

draw_poly(tess,8,50)

wn.mainloop()
