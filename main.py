

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

direction = "right" # initial directionS
x_axis = 0
y_axis = 0
score = 0
apple.goto(0,250)
apple.write(score)
apple.goto(random.choice(apple_positions), random.choice(apple_positions))

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
        

def check_bounds():
    global x_axis
    global y_axis
    if x_axis >= 14 or x_axis <= -16:
        turtle.bye()
    if y_axis >= 15 or y_axis <= -15:
        turtle.bye()
def check_self_collision():
    head = snake_segments[0]
    for segment in snake_segments[1:]:  # exclude the head
        if head.distance(segment) < 20:
            print("Collision with self!")
            turtle.bye()  # Ends the game


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
    if direction == "right":
        x_axis += 1
    if direction == "left":
        x_axis -= 1
    if direction == "up":
        y_axis += 1
    if direction == "down":
        y_axis -= 1
    screen.tracer(0)
    move_snake()
    check_bounds()
    check_self_collision()
    screen.update()
    collisions()
    
    time.sleep(0.15)
turtle.done()
