#!/bin/bash/python3

from turtle import Turtle
gloria = Turtle()

gloria.color('green')
gloria.shape('turtle')
gloria.penup()
gloria.goto(-160, 100)
gloria.pendown()


esther = Turtle()
ingram = Turtle()
eleven = Turtle()


esther.penup()
esther.goto(-160, 70)
esther.pendown()
esther.shape('turtle')
esther.color('grey')

ingram.penup()
ingram.goto(-160, 40)
ingram.pendown()
ingram.shape('turtle')
ingram.color('red')
ingram.shapesize(2)

eleven.penup()
eleven.goto(-160, 10)
eleven.pendown()
eleven.shape("turtle")
eleven.color("blue")

from random import randint
for movement in range(100):
    eleven.forward(randint(1,9))
    ingram.forward(randint(1,9))
    esther.forward(randint(1,9))
    gloria.forward(randint(1,9))

input("Press enter to close")

