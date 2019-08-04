# SquireSpiral2.py
# Billy Ridgeway
# Create a square spiral that rotates as it's being drawn.

import turtle           # Imports the turtle library.
t = turtle.Pen()        # Creates a new turtle called t.
t.speed(0)              # Sets the pen's speed to fast.

# Creates a for loop.
for x in range (100):   # Sets the range of x to 100.
    t.forward(2*x)      # Moves the pen forward 2 times the value of x.
    t.left(91)          # Sets the pen's direction left by 91 degrees.
