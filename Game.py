import turtle 

wn = turtle.Screen()
wn.title("Pong by @RedMattina")
wn.bgcolor("#990066")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A 
paddle_a=turtle.Turtle() #ftiaxnoume antikeimeno
paddle_a.speed(0)   #poso grhgora paei
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b=turtle.Turtle() #ftiaxnoume antikeimeno
paddle_b.speed(0)   #poso grhgora paei
paddle_b.shape("square")
paddle_b.color("#ffe6f7")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball=turtle.Turtle() #ftiaxnoume antikeimeno
ball.speed(1)   #poso grhgora paei
ball.shape("circle")
ball.color("#ffe6f7")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 


#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Limit the paddle's movement upwards
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:  # Limit the paddle's movement downwards
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Limit the paddle's movement upwards
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  # Limit the paddle's movement downwards
        y -= 20
    paddle_b.sety(y)


#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_up, "W")
wn.listen()
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_down, "S")

wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.listen()
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()

    #Move The Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290) 
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 


    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 


    #Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor()>paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
    
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor()>paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1