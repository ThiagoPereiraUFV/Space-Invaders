# Space Invaders v1.0 by Thiago Pereira
# Importing game essential modules
import turtle
import os
import time
import tkinter as tk

class SpaceInvaders :
	# Defining game entities
	def __init__(self) :
		root = tk.Tk()
		self.dimension = root.winfo_screenheight()*0.9
		self.Nenemies = 5
		self.NenemiesR = 5
		self.points = 0
		self.window, self.player, self.bullet = None, None, None
		self.enemies = []
		self.playerSpeed = 15*self.dimension*0.001
		self.bulletSpeed = 20*self.dimension*0.003
		self.enemySpeed = 2*self.dimension*0.003
		self.bulletState = "ready"

		self.createWindow()
		self.createPlayer()
		self.createPlayerBullet()
		self.createEnemies()
		self.main()

	def main(self) :
		# Listen keyboard
		turtle.listen()
		turtle.onkey(self.moveLeft, "Left")
		turtle.onkey(self.moveRight, "Right")
		turtle.onkey(self.fireBullet, "space")
		turtle.onkey(turtle.bye, "Escape")
		
		try:
			# Main game loop
			self.alertText("ready!", 2)
			self.alertText("go", 0.5)
			while True :
				# Enemies position
				for i in range(self.Nenemies) :
					if(self.enemies[i].isvisible()) :
						enemyX = self.enemies[i].xcor()
						enemyY = self.enemies[i].ycor()

						if(enemyX < -(self.dimension/2) + 40 or enemyX > (self.dimension/2) - 40) :
							self.enemySpeed *= -1

							for j in range(self.Nenemies) :
								if(self.enemies[j].isvisible()) :
									enemyX = self.enemies[j].xcor() + self.enemySpeed
									enemyY = self.enemies[j].ycor() - 30
									self.enemies[j].setposition(enemyX, enemyY)
						else:
							self.enemies[i].setposition(enemyX + self.enemySpeed, enemyY)
				
				# Bullet position
				if(self.bulletState == "fire") :
					bulletY = self.bullet.ycor()
					bulletY += self.bulletSpeed
					self.bullet.sety(bulletY)

					if(bulletY > (self.dimension/2)):
						self.bullet.hideturtle()
						self.bulletState = "ready"
				
				# Enemy death
				for i in range(self.Nenemies) :
					if(self.enemies[i].isvisible()) :
						rad = 15
						bulletX, bulletY = self.bullet.xcor(), self.bullet.ycor()
						enemyX, enemyY = self.enemies[i].xcor(), self.enemies[i].ycor()
						playerX, playerY = self.player.xcor(), self.player.ycor()
						if(bulletX > enemyX - rad and bulletX < enemyX + rad and bulletY > enemyY - rad and bulletY < enemyY + rad) :
							self.enemies[i].hideturtle()
							self.points += 1
							if(self.points == self.Nenemies) :
								self.alertText("You won!", 4)
								return

						if(enemyY > playerY - rad and enemyY < playerY + rad) :
							self.alertText("Game over!", 4)
							return
		finally:
			return

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


	# Defining and positioning player
	def createPlayer(self) :
		# Draw player
		self.player = turtle.Turtle()
		self.player.hideturtle()
		self.player.color("blue")
		self.player.shape("triangle")
		self.player.penup()
		self.player.speed(0)

		# Player initial position
		self.player.setposition(0, -(self.dimension/2) + 40)
		self.player.setheading(90)
		self.player.showturtle()

	# Defining and positioning player bullet
	def createPlayerBullet(self) :
		# Draw player bullet
		self.bullet = turtle.Turtle()
		self.bullet.hideturtle()
		self.bullet.color("yellow")
		self.bullet.shape("triangle")
		self.bullet.penup()
		self.bullet.speed(0)

		# Bullet initial position
		self.bullet.setposition(self.player.xcor(), self.player.ycor() + 10)
		self.bullet.setheading(90)
		self.bullet.shapesize(0.5, 0.5)

	# Defining and positioning enemy
	def createEnemies(self) :
		# Draw enemies
		row = 1
		col = 0
		for i in range(self.Nenemies) :
			if(i == row*5) :
				row += 1
				col = 0
			enemy = turtle.Turtle()
			enemy.hideturtle()
			enemy.color("red")
			enemy.shape("circle")
			enemy.penup()
			enemy.speed(0)
			enemy.setposition(-(self.dimension/2) + 40 + col*(self.dimension/self.NenemiesR), (self.dimension/2) - 40*row)
			enemy.showturtle()

			self.enemies.append(enemy)
			col += 1

	# Move spaceship left
	def moveLeft(self) :
		x = self.player.xcor()
		x -= self.playerSpeed

		if(x < -(self.dimension/2) + 40) :
			x = -(self.dimension/2) + 40

		self.player.setx(x)

	# Move spaceship right
	def moveRight(self) :
		x = self.player.xcor()
		x += self.playerSpeed

		if(x > (self.dimension/2) - 40) :
			x = (self.dimension/2) - 40

		self.player.setx(x)

	# Spaceship gun
	def fireBullet(self) :
		if(self.bulletState == "ready") :
			self.bulletState = "fire"
			self.bullet.setposition(self.player.xcor(), self.player.ycor() + 10)
			self.bullet.showturtle()

	def alertText(self, text, t) :
		self.bullet.hideturtle()
		turtle.hideturtle()
		turtle.color("yellow")
		style = ("Arial", 30)
		turtle.write(text.upper(), font=style, align="center")
		time.sleep(t)
		turtle.clear()

def main() :
	game = SpaceInvaders()

if __name__ == "__main__" :
	main()