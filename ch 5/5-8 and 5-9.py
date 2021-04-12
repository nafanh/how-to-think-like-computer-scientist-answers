import turtle
'''
Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled with yellow, and bars representing values less than 100 are filled with green.
'''
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    if height < 0:
        t.penup()
        t.forward(-15)
        t.write("  "+ str(height))
        t.forward(15)
        t.pendown()
    else:
        t.write("  " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()      # Added this line
    t.penup()
    t.forward(10)
    t.pendown()
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220, -50]
tess.speed(0)
for a in xs:
    if a >= 200:
        tess.color("blue","red")
    elif a >= 100 and a < 200:
        tess.color("blue","yellow")
    else:
        tess.color("blue","green")
    draw_bar(tess, a)

wn.mainloop()