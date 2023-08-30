# Unique
import turtle

# Setup
screen = turtle.Screen()  # Create a turtle screen
t = turtle.Turtle()       # Create a turtle object
t.speed(0)               # Set the drawing speed (0 is fastest)
t.left(90)               # Turn the turtle to face upwards
t.up()                   # Lift the pen
t.backward(200)          # Move the turtle backward (to position the base of the tree)
t.down()                 # Lower the pen to start drawing


# Draw the fractal tree
def fractal_tree(branch_length, level):

    if level == 0:        # Base case: stop recursion when level reaches 0
        return
    t.forward(branch_length)  # Draw the main branch
    t.left(45)                 # Turn left to draw left sub-branch
    fractal_tree(branch_length * 0.6, level - 1)  # Recursive call for left sub-branch
    t.right(90)                # Turn right to draw right sub-branch
    fractal_tree(branch_length * 0.6, level - 1)  # Recursive call for right sub-branch
    t.left(45)                 # Turn back to original direction
    t.backward(branch_length)  # Move the turtle back to the starting point


fractal = int(input("How far should this fractal go? "))  # Asks which fractal the program should run to
fractal_tree(100, fractal)  # Call the function to draw the fractal tree

# Finish
screen.exitonclick()  # Close the turtle graphics window when clicked and not immediately