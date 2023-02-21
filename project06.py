import turtle as t
import time

def right():
    t.goto(0,220)
    if ball.xcor()< 200:
        ball.forward(10)
    elif ball.xcor()>150:
        t.write("clear!", False,"center",("",30))
        t.color("white")
        
def left():
    if ball.xcor()> -200:
        ball.backward(10)
        
        

t.up()
t.speed(0)
t.setup(500,700)
t.goto(0,280)
t.write("Ball Game", False, "Center",("",35))

t.bgcolor("lightgreen")
t.setup(500,700)


#플레이어(ball)
ball=t.Turtle()
ball.shape("circle")
ball.shapesize(1.1)
ball.up()
ball.speed(0)
ball.color("white")
ball.goto(-190,-135)

#길
way=t.Turtle()
way.shape("square")
way.shapesize(1,20)
way.up()
way.speed(0)
way.goto(0,-270)

#도착
star=t.Turtle()
star.shape("turtle")
star.shapesize(2.2)
star.up()
star.speed(0)
star.color("yellow")
star.goto(190,-135)

#장애물1
wall=t.Turtle()
wall.shape("square")
wall.shapesize(1,)
wall.up()
wall.speed(0)
wall.goto(-100,-250)


#장애물2
wall2=t.Turtle()
wall2.shape("square")
wall2.shapesize(1,2)
wall2.up()
wall2.speed(0)
wall2.goto(100,-250)

t.listen()
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")
