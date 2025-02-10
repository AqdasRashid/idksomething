import turtle

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
fl = turtle.Turtle()
fl.speed(5)

# Function to draw a flag with a pole
def draw_flag_with_pole(x, y, flag_width, flag_height):
    # Draw the flag pole
    fl.penup()
    fl.goto(x - 10, y)  # Adjust for flagpole position
    fl.pendown()
    fl.color("black")
    fl.pensize(5)
    fl.setheading(270)  # Face downward
    fl.forward(flag_height * 1.5)  # Length of the flag pole

    # Reset to thin line
    fl.pensize(1)
    
    # Move to the flag's starting position
    fl.penup()
    fl.goto(x, y)
    fl.pendown()

    # Draw the flag rectangle
    fl.color("black", "red")
    fl.begin_fill()
    
    # Drawing the rectangle 
    fl.forward(flag_width)  # Top side
    fl.left(90)
    fl.forward(flag_height)  # Right side
    fl.left(90)
    fl.forward(flag_width)  # Bottom side
    fl.left(90)
    fl.forward(flag_height)  # Left side
    
    fl.end_fill()

# Function to draw a circle at a specific position
def draw_circle(x, y, radius):
    fl.penup()
    fl.goto(x, y)
    fl.pendown()
    fl.color("black", "white")  # Black outline, white fill
    fl.begin_fill()
    fl.circle(radius)
    fl.end_fill()

# Draw the first flag.
draw_flag_with_pole(-150, 100, 100, 150)
# Draw the circle for the first flag 
draw_circle(-75, 73, 20)  

# Draw the second flag.
draw_flag_with_pole(60, 75, 70, 100)
# Draw the circle for the second flag 
draw_circle(110, 55, 15)  

fl.hideturtle()
turtle.done()
