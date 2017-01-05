'''
Misha Alyas
Dec 5, 2015
Modify the program from Lab 11 to stop when the turtle wanders more than distance 100 from the starting point.
The current program uses a definite loop to always move 500 steps.
Change the program to use an indefinite loop that tests how far the turtle is from the origin.
When that distance exceeds 100, your program should stop. 
Hint: You only need to change the main() function of the exisiting program.
'''
import turtle
import random

def drawRing(t,radius,color):
    t.up()
    t.goto(0,-radius)
    t.color(color)
    t.down()
    t.circle(radius)

def setUpTurtle():

    t = turtle.Turtle()

    drawRing(t,100,"green")
    drawRing(t,200,"yellow")
    drawRing(t,300,"red")

    t.up()
    t.home()
    t.down()
    t.color("purple")
    t.shape("turtle")
    t.speed(100)

    return t

def main():
    tess = setUpTurtle()
    x,y=tess.pos()
    value=tess.distance((x,y),(0,0))
    while True:
        direction = random.random()
        if direction < 1/4:
            tess.right(90)
        elif direction < 1/2:
            tess.right(180)
        elif direction < 3/4:
            tess.left(90)
        tess.forward(10)
        x1,y1=tess.pos()
        value=tess.distance((x,y),(0,0))
        if value>=100:
            break
        
    turtle.Screen().exitonclick()

main()
