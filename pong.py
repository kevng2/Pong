# Kevin Nguyen
# Pong Game

import turtle

# defines control for each player
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

window = turtle.Screen() # Creates screen for game
window.title("Kevin Nguyen Pong") # title of window
window.bgcolor("black") #background color
window.setup(width = 800, height = 600) # dimensions of window
window.tracer(0) # stops window from updating

# Paddle A
paddleA = turtle.Turtle() # creating a Turtle object
paddleA.speed(0) # speed of paddle animation
paddleA.shape("square") # gives paddle a shape
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.color("white")
paddleA.penup() # prevents line drawing
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle() 
paddleB.speed(0) 
paddleB.shape("square") 
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.color("white")
paddleB.penup() 
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape("circle") 
ball.color("white")
ball.penup() 
ball.goto(0, 0)

# values will be used later to move the ball
ball.dx = 4 
ball.dy = 4 

window.listen() # listen to user input

# Player 1
window.onkeypress(paddleA_up, "w") # binds the "w" to the up function
window.onkeypress(paddleA_down, "s")

# Player 2
window.onkeypress(paddleB_up, "Up")
window.onkeypress(paddleB_down, "Down")

# main game loop
while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Make balls bounce off of the window border 
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.dx *= -1

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0,0)

    # Checking if Ball will hit the paddles
    if ball.xcor() < -200:
        if ball.xcor() <= paddleA.xcor() + 5 and ball.ycor() <= paddleA.ycor() + 5 or (ball.xcor() <= paddleA.xcor() + 5 and ball.ycor() >= paddleA.ycor() - 5):
            ball.dx *= -1


