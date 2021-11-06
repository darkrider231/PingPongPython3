# Simple Pong Game in Python 3 for Beginners
# I am trying to learn Python 3
# FreeCodeCamp: https://www.youtube.com/watch?v=XGf2GcyHPhc&t=2346s
import turtle
import winsound


wn = turtle.Screen()
wn.title("Simple Ping Pong created in Python 3: edited by GrantsGaming")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) 


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-140, 260)
pen.color("red")
pen.write("Player A: 0", align="center", font=("Courier", 20, "bold"))
pen.color("blue")
pen.goto(140, 260)
pen.write("Player B: 0", align="center", font=("Courier", 20, "bold"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()

# Key Presses for Paddle A
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# Key Presses for Paddle B
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.goto(140, 260)
        pen.clear()
        pen.color("blue")
        pen.write("Player B: {}".format(score_b), align="center", font=("Courier", 20, "bold"))
        pen.goto(-140, 260)
        pen.color("red")
        pen.write("Player A: {}".format(score_a), align="center",  font=("Courier", 20, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.goto(-140, 260)
        pen.clear()
        pen.color("red")
        pen.write("Player A: {}".format(score_a), align="center", font=("Courier", 20, "bold"))
        pen.goto(140, 260)
        pen.color("blue")
        pen.write("Player B: {}".format(score_b), align="center", font=("Courier", 20, "bold"))


    # Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)