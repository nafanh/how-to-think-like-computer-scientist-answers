import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
# The next four functions are our "event handlers".
p_size = 3
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()

# Close down the turtle window

def green():
    tess.color("green")

def red():
    tess.color("red")

def blue():
    tess.color("blue")

def plus():
    global p_size
    if p_size <= 18:
        p_size += 2
        tess.pensize(p_size)
def minus():
    global p_size
    if p_size >= 3:
        p_size -= 2
        tess.pensize(p_size)



def k():
    wn.title("LEL")
# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(green,"g")
wn.onkey(red,"r")
wn.onkey(blue,"b")
wn.onkeypress(plus,"+")
wn.onkeypress(minus,"-")
wn.onkey(k,"k")


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()


