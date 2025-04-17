import turtle

screen = turtle.Screen()
t1 = turtle.Turtle()
t1.width(10)
t1.color("red")
t1.speed(0)

direction = "right"

def move_up():
    global direction
    if direction != "down":
        direction = "up"
        y = t1.ycor()
        t1.speed(0)
        t1.seth(90)
        t1.speed(5)
    

def move_down():
    direction = "down"
    y = t1.ycor()
    t1.speed(0)
    t1.seth(270)
    t1.speed(5)
    

def move_left():
    direction = "left"
    x = t1.xcor()
    t1.speed(0)
    t1.seth(180)
    t1.speed(5)
    

def move_right():
    direction = "right"
    x = t1.xcor()
    t1.speed(0)
    t1.seth(0)
    t1.speed(5)
    

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

while True:
    t1.forward(1)





t1.forward(100)

turtle.done()
