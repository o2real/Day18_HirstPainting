# import colorgram
#
# rgb_colors =[]
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
color_list = [(133, 164, 201), (224, 151, 102), (31, 43, 63), (200, 136, 148), (160, 61, 51), (235, 212, 91), (46, 100, 143), (137, 181, 161), (148, 63, 71), (57, 48, 45), (160, 32, 28), (60, 115, 99), (52, 41, 45), (236, 166, 157), (170, 29, 34), (230, 164, 169), (212, 84, 74), (35, 61, 56), (14, 96, 71), (34, 60, 105), (171, 188, 220), (196, 98, 106), (109, 126, 157), (19, 83, 104), (174, 200, 190), (64, 66, 56)]

tim.ht()
tim.up()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
