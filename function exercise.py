import turtle

def triangel(x):
    for i in range(3):
        turtle.forward(150)
        turtle.left(120)

counter = 0
while counter < 1:
    triangel(30)
    turtle.right(4)
    counter += 1
turtle.exitonclick()
