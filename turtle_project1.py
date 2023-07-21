import turtle
m=turtle.Screen()
m.title("pattern project on Turtle by Abhishek Kumar Singh from Cap01")
turtle.bgcolor('black')
turtle.speed(20)
turtle.pensize(1)
colors=('blue','orange','yellow','dark','green','red')
for i in range(200):
    turtle.fd(i*4)
    turtle.right(90)
    turtle.color(colors[i%5])


    for j in range(3):
        turtle.fd(j*4)
        turtle.right(90)

        for k in range(2):
            turtle.fd(k*4)
            turtle.right(90)

            for l in range(739):
                turtle.fd(l*4)
                turtle.right(891)
