import turtle

# Initialize the turtle
t = turtle.Turtle()


# Function to move the turtle forward
def move_forward():
    t.forward(10)


# Function to move the turtle backward
def move_backward():
    t.backward(10)


# Function to rotate the turtle clockwise
def rotate_clockwise():
    t.right(10)


# Function to rotate the turtle counterclockwise
def rotate_counterclockwise():
    t.left(10)


# Function to clear the drawing and bring the turtle to origin
def clear_drawing():
    t.clear()
    t.penup()
    t.home()
    t.penup()


# Setup input handling and event listener
turtle.listen()
turtle.onkeypress(move_forward, 'w')
turtle.onkeypress(move_backward, 's')
turtle.onkeypress(rotate_clockwise, 'd')
turtle.onkeypress(rotate_counterclockwise, 'a')
turtle.onkeypress(clear_drawing, 'c')

# Keep the window open
turtle.done()
