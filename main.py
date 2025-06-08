# import colorgram
#
# rgb_colours = []
# colours = colorgram.extract('image.jpeg', 30)
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
# print(rgb_colours)
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colour_set = [(231, 236, 241), (236, 244, 241), (203, 165, 108),
              (37, 99, 133), (126, 83, 54), (127, 164, 189), (233, 206, 107), (173, 149, 42),
              (199, 75, 111), (223, 127, 145), (141, 55, 74), (119, 39, 70), (57, 46, 43),
              (86, 169, 116), (221, 67, 53), (105, 196, 190), (245, 160, 170),
              (66, 108, 77),(42, 157, 203), (2, 61, 85), (60, 53, 58), (214, 182, 177),
              (88, 50, 45), (153, 212, 198),(126, 119, 159), (60, 56, 103), (17, 89, 100),
              (160, 205, 215)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_position in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_set))
    tim.forward(50)

    if dot_position % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


turtle.exitonclick()

