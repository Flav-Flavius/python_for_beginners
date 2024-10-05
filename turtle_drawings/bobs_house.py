# a program that builds a house for bob the turtle
import turtle
import math
wn = turtle.Screen()
bob = turtle.Turtle()
bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.right(135)
# sometimes is better to use some math instead of guessing :)
dist = math.sqrt(50 * 50 // 2)
bob.forward(dist)
bob.right(90)
bob.forward(dist)