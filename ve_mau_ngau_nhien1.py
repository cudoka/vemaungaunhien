import turtle
import random

number = random.uniform(0,3)
print(number)

if (number <= 1):
    color = "blue"
elif (number <= 2):
    color = "yellow"
else:
    color = "red"

turtle.bgcolor("black")
turtle.shape("turtle")
turtle.color(color)
turtle.done()