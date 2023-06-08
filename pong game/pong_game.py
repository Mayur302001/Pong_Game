import turtle
import winsound


wd = turtle.Screen()
wd.title("PONG GAME BY YOUR ALLY")
wd.bgcolor("yellow")
wd.setup(width = 800,height = 600)
wd.tracer(0)

#Score

score_a = 0
score_b = 0

#paddle A

paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0) 
paddle_a.penup()
paddle_a.color("blue")
paddle_a.goto(-350 , 0)
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)

#paddle B

paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)

#Ball

ball =turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.speed(2)
ball.goto(0,0)
ball.penup()
ball.dx = 0.14
ball.dy = -0.14

#scoreboard

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0  Player B:0", align= "center", font =("Courier" , 15, "normal"))

# Function

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
# Key Binds

wd.listen()
wd.onkeypress(paddle_a_up,"w")
wd.onkeypress(paddle_a_down,"s")
wd.onkeypress(paddle_b_up, "Up")
wd.onkeypress(paddle_b_down, "Down")


# main game
while True:
    wd.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align= "center", font =("Courier" , 15, "normal"))
        


    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align= "center", font =("Courier" , 15, "normal"))
        
        


    # ball and paddle collide

    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1   
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)








