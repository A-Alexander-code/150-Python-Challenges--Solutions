import turtle
import random

lines = random.randint(5,20)

for x in range(0,lines):
    lenght = random.randint(25,100)
    rotate = random.randint(1,365)
    turtle.forward(lenght)
    turtle.right(rotate)
    
turtle.exitonclick()