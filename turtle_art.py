import turtle as t
import random
tt = t.Turtle()

t.colormode(255)
color_list = [(19, 105, 173), (168, 12, 69), (224, 148, 83), (150, 59, 109), (191, 72, 20), (213, 72, 136), (79, 15, 49), (213, 124, 173), (102, 162, 223), (25, 189, 134), (9, 45, 86), (205, 154, 14), (23, 52, 146), (85, 96, 220), (224, 210, 88), (103, 192, 131), (233, 80, 45), (236, 200, 224), (13, 170, 210), (238, 203, 179), (193, 216, 248), (35, 134, 107), (174, 22, 12), (235, 160, 200), (168, 175, 240), (187, 226, 5), (3, 91, 112), (121, 234, 131), (68, 33, 21), (238, 167, 157)]

tt.hideturtle()
tt.penup()
tt.setheading(220)
tt.forward(280)
tt.setheading(0)
tt.speed("fastest")
number_of_dots = 100

for dots in range(1,number_of_dots+1):
    tt.dot(20, random.choice(color_list))
    tt.forward(40)
    if dots % 10 == 0:
        tt.setheading(90)
        tt.forward(50)
        tt.setheading(180)
        tt.forward(400)
        tt.setheading(0)

screen = t.Screen()
screen.exitonclick()
