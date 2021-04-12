import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()
green_t = turtle.Turtle()
yellow_t = turtle.Turtle()
red_t = turtle.Turtle()

green_t.color("green")
yellow_t.color("yellow")
red_t.color("red")

green_t.penup()
yellow_t.penup()
red_t.penup()

green_t.forward(40)
yellow_t.forward(40)
red_t.forward(40)

green_t.left(90)
yellow_t.left(90)
red_t.left(90)

green_t.forward(50)
green_t.pendown()

yellow_t.forward(100)
yellow_t.pendown()

red_t.forward(150)
red_t.pendown()


tess.penup()
tess.forward(100)
tess.pendown()
draw_housing()


tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

red_t.hideturtle()
yellow_t.hideturtle()
green_t.hideturtle()
def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        yellow_t.showturtle()
        green_t.hideturtle()
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        red_t.showturtle()
        yellow_t.hideturtle()
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        green_t.showturtle()
        yellow_t.hideturtle()
        red_t.hideturtle()
    wn.ontimer(advance_state_machine,60)

# Bind the event handler to the space key.
advance_state_machine()                   # Listen for events
wn.listen()
wn.mainloop()