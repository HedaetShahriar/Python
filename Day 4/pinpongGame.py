import turtle
screen= turtle.Screen()
screen.title("PingPong")
screen.bgcolor("White")
screen.setup(width=800,height=600)
screen.tracer(0)
#Left Bar
paddle1=turtle.Turtle()
paddle1.shape("square")
paddle1.color("Black")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-370,0)
#Right Bar
paddle2=turtle.Turtle()
paddle2.shape("square")
paddle2.color("Black")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(370,0)

def paddle1Up():
    y=paddle1.ycor()
    y+=5
    if y<=250:
        paddle1.sety(y)

def paddle2Up():
    y=paddle2.ycor()
    y+=5
    if y<=250:
        paddle2.sety(y)

def paddle1Down():
    y=paddle1.ycor()
    y-=5
    if y>=-250:
        paddle1.sety(y)

def paddle2Down():
    y=paddle2.ycor()
    y-=5
    if y>=-250:
        paddle2.sety(y)       
screen.listen()
screen.onkeypress(paddle1Down,"s")
screen.onkeypress(paddle1Up,"w")
screen.onkeypress(paddle2Up,"Up")
screen.onkeypress(paddle2Down,"Down")
print("Start")
while(1):
    screen.update()