import time
import turtle

screen = turtle.Screen()

t1 = turtle.Turtle()
t1.hideturtle()
t1.width(5)
t1.color("red")
t1.speed(0)

t2 = turtle.Turtle()
t2.hideturtle()
t2.width(10)
t2.color("yellow")
t2.backward(50)

t3 = turtle.Turtle()
t3.hideturtle()
t3.width(10)
t3.color("blue")



direction = "right"



def move_up():
    global direction
    if direction != "down":
        direction = "up"
        t1.speed(0)
        t1.seth(90)
        t1.speed(5)

def move_down():
    global direction
    if direction != "up":
        direction = "down"
        t1.speed(0)
        t1.seth(270)
        t1.speed(5)

def move_left():
    global direction
    if direction != "right":
        direction = "left"
        t1.speed(0)
        t1.seth(180)
        t1.speed(5)

def move_right():
    global direction
    if direction != "left":
        direction = "right"
        t1.speed(0)
        t1.seth(0)
        t1.speed(5)

def test():
    print("nothing")

def eraseHorizontal():
    t2.seth(t1.heading())
    t2.forward(1)

def eraseVertical(): #finished here
    t3.penup()
    t3.speed(0)
    t3.goto(t1.position())

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")


while True:
    t1.forward(1)
    screen.ontimer(eraseHorizontal,1)


turtle.done()
