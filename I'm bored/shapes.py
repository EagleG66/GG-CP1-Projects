import turtle

def draw(shape, x, y, unit, thickness=10, speed=0):

    if shape == "square":
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(speed)
        pen.width(thickness)
        pen.shape("square")
        pen.teleport(x+unit,y-unit)
        for i in range(4):
            pen.left(90)
            pen.forward(unit*2)

draw("square", -500, 400, 25, 15, 3)