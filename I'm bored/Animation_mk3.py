import turtle as t
import time

cannon = t.Turtle()

time.sleep(3)

cannon.shape("square")
cannon.width(50)
cannon.color("gray")
cannon.teleport(350, -100)
cannon.forward(200)
cannon.left(90)
cannon.forward(50)
cannon.left(90)
cannon.forward(200)
cannon.left(90)
cannon.forward(50)

cannon_tread = t.Turtle()
cannon_tread.speed(1)
cannon_tread.shape("square")
cannon_tread.teleport(370, -100)
cannon_tread.width(75)
cannon_tread.forward(200)

cannon_barrel = t.Turtle()
cannon_barrel.shape("square")
cannon_barrel.width(40)
cannon_barrel.color("gray")
cannon_barrel.teleport(340, -50)
cannon_barrel.left(170)
cannon_barrel.forward(150)

cannon_ball = t.Turtle()
cannon_ball.shape("circle")
cannon_ball.teleport(190, -25)
cannon_ball.up()
cannon_ball.width(35)
cannon_ball.speed(10)
cannon_ball.left(170)
cannon_ball.forward(250)
cannon_ball.speed(100)
for i in range(40):
    cannon_ball.forward(24)
    cannon_ball.left(1)

time.sleep(2)






