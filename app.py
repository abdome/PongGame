#import turtle for graphics
import turtle

#make the window
wind=turtle.Screen()
#title for screen
wind.title("Ping Pong")
#background and width and height
wind.bgcolor("black")
wind.setup(width=600,height=400)
#prevent any update from window
wind.tracer(0)
#madrab1
madrab1=turtle.Turtle()
madrab1.speed(0)#speed for animation high is 0
madrab1.shape("square")# shape of object
madrab1.color("blue") #color
madrab1.shapesize(stretch_wid=5,stretch_len=1)#stretch width in yaxis by 5*20
madrab1.penup()#remove lines
madrab1.goto(-250,0)
#function for moving madrab1
def madrab1_up():
    y = madrab1.ycor()# getting y point
    if y<=130:
        y+=10
    madrab1.sety(y)
def madrab1_down():
    y=madrab1.ycor()
    if(y>=-130):
        y-=10
    madrab1.sety(y)
#connect keybord
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down,"s")
#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(250,0)
#function for madrab2
def madrab2_up():
    y=madrab2.ycor()
    if(y>=130):
        y+=10
    madrab2.sety(y)

def madrab2_down():
    y=madrab2.ycor()
    if(y>=-130):
        y-=10
    madrab2.sety(y)
wind.listen()
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1
#function for ball

#looping the window
while True:
    wind.update()
    #moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1
    if ball.ycor()<-190:
        ball.sety(-190)
        ball.dy*=-1
    if ball.xcor()>290 :
        ball.goto(0,0)
        ball.dx*=-1
    if ball.xcor()<-290 :
        ball.goto(0, 0)
        ball.dx*=-1

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<madrab1.ycor()+40 and ball.ycor()>madrab1.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1


