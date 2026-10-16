import turtle

t = turtle.Turtle()
t.speed(5)

# Set background
turtle.bgcolor("white")

# Function to draw rectangle
def rectangle(color, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()

# Draw three stripes
rectangle("orange", -300, 150, 600, 100)
rectangle("white", -300, 50, 600, 100)
rectangle("green", -300, -50, 600, 100)

# Draw Ashoka Chakra
t.penup()
t.goto(0, -50)
t.setheading(0)
t.pendown()
t.pencolor("navy")
t.pensize(3)
t.circle(50)

# Draw 24 spokes
for i in range(24):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 15)
    t.forward(50)
    t.pendown()
    t.goto(0, 0)

# Flag pole
t.penup()
t.goto(-300, 150)
t.pendown()
t.pencolor("black")
t.pensize(5)
t.goto(-300, -400)

# Pole base
t.penup()
t.goto(-350, -400)
t.pendown()
t.forward(100)

turtle.done()