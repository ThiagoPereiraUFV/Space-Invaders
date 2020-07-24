# Space Invaders v1.0 by Thiago Pereira
import turtle
import os

# Defining screen window
def createWindow() :
	# Create window
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Space Invaders v1.0 by Thiago Pereira")

	# Draw border
	border_pen = turtle.Turtle()
	border_pen.speed(0)
	border_pen.color("white")
	border_pen.penup()
	border_pen.setposition(-270, -270)
	border_pen.pendown()
	border_pen.pensize(3)

	for side in range(4) :
		border_pen.fd(540)
		border_pen.lt(90)

	border_pen.hideturtle()

	return window

def main() :
	window = createWindow()

	value = input("Press enter to exit")

if __name__ == "__main__" :
	main()