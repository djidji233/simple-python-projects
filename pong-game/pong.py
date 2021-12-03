import turtle

wn = turtle.Screen()
wn.title("MyPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # stops window auto updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # animation speed (max)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0) # 0,0 is the middle

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # sets to max speed for animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) # 0,0 is the middle

# Ball
ball = turtle.Turtle()
ball.speed(0) # sets to max speed for animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0) # 0,0 is the middle
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("A: {}  B: {}".format(score_a,score_b), align="center", font=("Courier",24, "bold"))

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

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check border
    if ball.ycor() > 295:
        ball.sety(295)
        ball.dy *= -1
    
    if ball.ycor() < -295:
        ball.sety(-295)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("A: {}  B: {}".format(score_a,score_b), align="center", font=("Courier",24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("A: {}  B: {}".format(score_a,score_b), align="center", font=("Courier",24, "bold"))

    # Paddle bounce
    if (350 > ball.xcor() > 340) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1


   