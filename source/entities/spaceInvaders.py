# Importing game essential modules
import turtle
import os
import time
import tkinter as tk

# Importing game entities
from .player import Player
from .enemies import Enemies

class SpaceInvaders :
	# Defining game entities
	def __init__(self, level) :
		# Setting board size
		root = tk.Tk()
		self.dimension = root.winfo_screenheight()*0.9

		# Setting color, number and enemies by row
		self.nEnemies = 5
		self.nEnemiesR = 5
		self.color = ["yellow", "gold", "orange", "red", "maroon", 
		"violet", "magenta", "purple", "navy", "blue", "skyblue", 
		"cyan", "turquoise", "lightgreen", "green", "darkgreen", 
		"chocolate", "brown", "gray", "white"]

		# Game level
		self.level = level

		# Start the game
		self.main()

	def main(self) :
		# Game level loop
		while True :
			# Setting initial point and level state
			points = 0
			nextLevel = False

			# Setting game entities
			self.createWindow()
			player = Player(self.dimension)
			enemies = Enemies(self.nEnemies, self.nEnemiesR, self.color, self.level, self.dimension)

			try :
				# Listen keyboard
				turtle.listen()
				turtle.onkey(player.moveLeft, "Left")
				turtle.onkey(player.moveRight, "Right")
				turtle.onkey(player.fireBullet, "space")
				turtle.onkey(turtle.bye, "Escape")
			
				self.alertText("level " + str(self.level), 2)
				self.alertText("ready!", 1)
				self.alertText("go", 0.5)

				# Game main loop
				while True :
					# Enemies position
					for i in range(self.nEnemies) :
						if(enemies[i].isvisible()) :
							enemyX = enemies[i].xcor()
							enemyY = enemies[i].ycor()


							if(enemyX < -(self.dimension/2) + 40 or enemyX > (self.dimension/2) - 40) :
								enemies.speed *= -1

								for j in range(self.nEnemies) :
									if(enemies[j].isvisible()) :
										enemyX = enemies[j].xcor() + enemies.speed
										enemyY = enemies[j].ycor() - 30
										enemies[j].setposition(enemyX, enemyY)
							else:
								enemies[i].setposition(enemyX + enemies.speed, enemyY)

					# Bullet position
					if(player.bulletState == "fire") :
						bulletY = player.bullet.ycor()
						bulletY += player.bulletSpeed
						player.bullet.sety(bulletY)

						if(bulletY > (self.dimension/2)):
							player.bullet.hideturtle()
							player.bulletState = "ready"

					# Enemy death
					for i in range(self.nEnemies) :
						if(enemies[i].isvisible()) :
							rad = 15
							bulletX, bulletY = player.bullet.xcor(), player.bullet.ycor()
							enemyX, enemyY = enemies[i].xcor(), enemies[i].ycor()
							playerX, playerY = player.player.xcor(), player.player.ycor()
							if(bulletX > enemyX - rad and bulletX < enemyX + rad and bulletY > enemyY - rad and bulletY < enemyY + rad) :
								enemies[i].hideturtle()
								points += 1
								if(points == self.nEnemies) :
									self.alertText("You won!", 4)
									turtle.resetscreen()
									nextLevel = True
									break
							
							if(enemyY > playerY - rad and enemyY < playerY + rad) :
								self.alertText("Game over!", 4)
								turtle.bye()

					if(nextLevel) :
						break
			except :
				break

			self.level += 1

	# Defining screen window
	def createWindow(self) :
		# Create window
		self.window = turtle.Screen()
		self.window.setup(width=1.0, height=1.0, startx=None, starty=None)
		self.window.bgcolor("black")
		self.window.title("Space Invaders v1.0 by Thiago Pereira")

		# Draw border
		border_pen = turtle.Turtle()
		border_pen.hideturtle()
		border_pen.speed(0)
		border_pen.color("white")
		border_pen.penup()
		border_pen.setposition(-(self.dimension/2), -(self.dimension/2))
		border_pen.pendown()
		border_pen.pensize(5)

		for side in range(4) :
			border_pen.fd(self.dimension)
			border_pen.lt(90)

	def alertText(self, text, t) :
		turtle.hideturtle()
		turtle.color("yellow")
		style = ("Arial", 30)
		turtle.write(text.upper(), font=style, align="center")
		time.sleep(t)
		turtle.clear()