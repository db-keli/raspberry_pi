import turtle
import RPi.GPIO as GPIO

# NAME = "Mike"
# PASSWORD = "2345"
# username = input("What's your name?\n")
# password = input("password: ")

# if NAME == username and password == PASSWORD:
#     print("You're Welcome to Raspberry Pi Os")
#     while True:
#         turtle.forward(90)
#         turtle.right(50)
    
    
# else :
#     print("You're an imposter Bro!!")

pat = turtle.Turtle()
col = turtle.Screen()
col.bgcolor('blue')
pat.color('cyan')

for i in range(10):
    for i in range(2):
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120) 

