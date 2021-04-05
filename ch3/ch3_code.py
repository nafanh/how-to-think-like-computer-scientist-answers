'''
Write a program that prints We like Python's turtles! 1000 times.
'''
for i in range(1000):
    print("We like Python's turtles!")

'''
Write a program that uses a for loop to print

'''

months = ['January','February','March','April','May','June','July','August',
          'September','November','December']
for month in months:
    print("One of the months of the year is",month)

'''Suppose our turtle tess is at heading 0 — facing east. We execute the statement tess.left(3645). What does tess 
do, and what is her final heading? 
The turtle will spin around 10 times and the point 15 degrees left from its starting point in the end
'''

'''
Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

Write a loop that prints each of the numbers on a new line.
Write a loop that prints each number and its square on a new line.
Write a loop that adds all the numbers from the list into a variable called total. You should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed.
Print the product of all the numbers in the list. (product means all multiplied together)
'''
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for num in xs:
    print(num)

for num in xs:
    print(num**2)

total = 0
for num in xs:
    total += num
print(total)

product = 1
for num in xs:
    product *= num
print(product)

'''
Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

An equilateral triangle
A square
A hexagon (six sides)
An octagon (eight sides)
'''

#Eq triangle
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
for i in range(3):
    tess.left(120)
    tess.forward(100)

wn.mainloop()

#Square
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
for i in range(4):
    tess.left(90)
    tess.forward(100)
wn.mainloop()

#hexagon
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
for i in range(6):
    tess.left(60)
    tess.forward(100)
wn.mainloop()

#octagon
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
for i in range(8):
    tess.left(360/8)
    tess.forward(100)
wn.mainloop()

'''A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 
steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 
steps are taken. Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are 
counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. '''

#Enhance your program above to also tell us what the drunk pirate’s heading is after he has finished stumbling around.
# (Assume he begins at heading 0).
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
turns =  [160, -43, 270, -97, -43, 200, -940, 17, -86]
for turn in turns:
    print("Pirate is turning",turn,"degrees")
    tess.left(turn)
    tess.forward(100)

wn.mainloop()



#Draw a star
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
for i in range(5):
    tess.right(144)
    tess.forward(100)
tess.hideturtle()
wn.mainloop()

#Draw clock
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.shape('turtle')
tess.pensize(3)
tess.color('blue')
tess.stamp()
tess.penup()

for i in range(12):
    tess.forward(80)
    tess.pendown()
    tess.forward(10)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.forward(-110)
    tess.left(30)

wn.mainloop()