import turtle as t
import random
from turtle import Screen
new_turtle = t.Turtle()

new_turtle.pensize(2)
new_turtle.speed(30)

t.colormode(255)
def draw_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for _ in range(100):
    new_turtle.color(draw_colors())
    new_turtle.circle(100)
    new_turtle.left(10)

screen = Screen()
screen.exitonclick()