""" 
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
t2.color("blue")
t2.backward(50)

t3 = turtle.Turtle()
t3.hideturtle()
t3.width(10)
t3.color("yellow")



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


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

def eraseHorizontal():
    t2.seth(t1.heading())
    t2.forward(2)

    global direction
    t3.speed(0)
    if direction == "up":
        t3.pendown()
        t3.goto(t1.xcor(), t1.ycor() - 50)



while True:
    t1.forward(2)
    screen.ontimer(eraseHorizontal,1)


turtle.done()
"""

import turtle
import random
import time

#random_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

screen = turtle.Screen()
screen.setup(width=600, height=600)  # You can also let it default

#positions from –280 up to +280 in steps of 20
apple_positions = list(range(-280, 281, 20))

apple = turtle.Turtle("square")
apple.speed(0)
apple.penup()
apple.color("red")
apple.goto(random.choice(apple_positions), random.choice(apple_positions))

direction = "right" # initial directionS


snake_segments = []

speed = 3
def add_segment(position):
    global speed
    segment = turtle.Turtle("square")
    segment.color("green")
    segment.penup()
    segment.speed(0)
    segment.goto(position)
    segment.speed(speed)
    snake_segments.append(segment)
def move_snake():
    # Move segments from tail to head
    for i in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[i - 1].xcor()
        new_y = snake_segments[i - 1].ycor()
        snake_segments[i].goto(new_x, new_y)
    
    # Move the head
    head = snake_segments[0]
    if direction == "up":
        head.sety(head.ycor() + 20)
    elif direction == "down":
        head.sety(head.ycor() - 20)
    elif direction == "left":
        head.setx(head.xcor() - 20)
    elif direction == "right":
        head.setx(head.xcor() + 20)

def collisions():
    if snake_segments[0].position() == apple.position():
        add_segment(apple.position())
        apple.goto(random.choice(apple_positions), random.choice(apple_positions))

def move_up():
    global direction
    if direction != "down":
        direction = "up"
def move_down():
    global direction
    if direction != "up":
        direction = "down"

def move_left():
    global direction
    if direction != "right":
        direction = "left"

def move_right():
    global direction
    if direction != "left":
        direction = "right"
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

add_segment((0, 0)) # first 3 segments
add_segment((-20,0))
add_segment((-40,0))



while True:
    screen.tracer(0)
    move_snake()
    screen.update()
    collisions()
    time.sleep(0.15)
turtle.done()
