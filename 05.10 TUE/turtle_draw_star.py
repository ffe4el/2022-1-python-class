import turtle

star = turtle.Turtle()

star.right(72)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()