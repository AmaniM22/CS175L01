import math
import turtle
#Amani Minaya
#CSL-175
#Turtle Assignment
# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Initialize the turtle.
arrow = turtle.Turtle()
arrow.color("red")
arrow.begin_fill()

# Move the turtle to the starting point.
arrow.goto(0,diameter-s)

# Draw the octagon.
arrow.begin_fill()
for i in range(NUM_SIDES):
    arrow.forward(s)
    arrow.right(ANGLE)
arrow.end_fill()
# Display 'STOP'
arrow.color('white')
arrow.goto(TEXT_X,TEXT_Y)
arrow.write('STOP', font=('Impact','55'))

                         



