import turtle as t
import time
import random


time.sleep(3)


def leftCannon():

    cannon = t.Turtle()
    cannon.shape("square")
    cannon.width(50)
    cannon.color("gray")
    cannon.teleport(-350, -100)
    cannon.right(180)
    cannon.forward(200)
    cannon.right(90)
    cannon.forward(50)
    cannon.right(90)
    cannon.forward(200)
    cannon.right(90)
    cannon.forward(50)

    cannon_tread = t.Turtle()
    cannon_tread.speed(1)
    cannon_tread.shape("square")
    cannon_tread.teleport(-350, -110)
    cannon_tread.right(180)
    cannon_tread.width(75)
    cannon_tread.forward(210)

    cannon_axel = t.Turtle()
    cannon_axel.shape("circle")
    cannon_axel.color("gray")
    cannon_axel.width(50)
    cannon_axel.teleport(-350, -110)
    cannon_axel.right(180)
    cannon_axel.forward(1)
    cannon_axel.teleport(-560, -110)
    cannon_axel.forward(1)

    cannon_barrel = t.Turtle()
    cannon_barrel.shape("square")
    cannon_barrel.width(40)
    cannon_barrel.color("gray")
    cannon_barrel.teleport(-340, -50)
    cannon_barrel.right(180)
    cannon_barrel.right(170)
    cannon_barrel.forward(150)


def leftShoot(length):
    cannon_ball = t.Turtle()
    cannon_ball.shape("circle")
    cannon_ball.teleport(-190, -25)
    cannon_ball.right(180)
    cannon_ball.up()
    cannon_ball.width(35)
    cannon_ball.speed(10)
    cannon_ball.right(170)
    cannon_ball.forward(250)
    cannon_ball.speed(100)
    for i in range(40):
        cannon_ball.forward(length)
        cannon_ball.right(1)



def rightCannon():

    cannon = t.Turtle()
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
    cannon_tread.teleport(350, -110)
    cannon_tread.width(75)
    cannon_tread.forward(210)

    cannon_axel = t.Turtle()
    cannon_axel.shape("circle")
    cannon_axel.color("gray")
    cannon_axel.width(50)
    cannon_axel.teleport(350, -110)
    cannon_axel.forward(1)
    cannon_axel.teleport(560, -110)
    cannon_axel.forward(1)

    cannon_barrel = t.Turtle()
    cannon_barrel.shape("square")
    cannon_barrel.width(40)
    cannon_barrel.color("gray")
    cannon_barrel.teleport(340, -50)
    cannon_barrel.left(170)
    cannon_barrel.forward(150)



def rightShoot(length):
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
        cannon_ball.forward(length)
        cannon_ball.left(1)




leftCannon()

rightCannon()

while True:
    leftShoot(random.randint(1,25))

    rightShoot(random.randint(1,25))

time.sleep(2)






