# Space Invaders v1.0 by Thiago Pereira
import turtle
import os

class SpaceInvaders :
	# Defining game entities
	def __init__(self) :
		self.window = None
		self.player = None
		self.bullet = None
		self.enemy = None
		self.playerSpeed = 15
		self.bulletSpeed = 15
		self.enemySpeed = 3
		self.bulletState = "ready"

		self.createWindow()
		self.createPlayer()
		self.createPlayerBullet()
		self.createEnemy()
		self.main()

	def main(self) :
		# Listen keyboard
		turtle.listen()
		turtle.onkey(self.moveLeft, "Left")
		turtle.onkey(self.moveRight, "Right")
		turtle.onkey(self.fireBullet, "space")
		turtle.onkey(turtle.bye, "Escape")

		# Main game loop
		while True :
			# Enemy position
			enemyX = self.enemy.xcor()
			enemyY = self.enemy.ycor()
			enemyX += self.enemySpeed

			if(enemyX > 230) :
				enemyY -= 30
				self.enemySpeed *= -1
			elif(enemyX < -230) :
				enemyY -= 30
				self.enemySpeed *= -1

			self.enemy.setx(enemyX)
			self.enemy.sety(enemyY)

			# Bullet position
			bulletY = self.bullet.ycor()
			bulletY += self.bulletSpeed
			self.bullet.sety(bulletY)

			if(bulletY > 270):
				self.bullet.hideturtle()
				self.bulletState = "ready"

			# Enemy death
			bulletX, bulletY = self.bullet.xcor(), self.bullet.ycor()
			enemyX, enemyY = self.enemy.xcor(), self.enemy.ycor()
			if(bulletX > enemyX - 10 and bulletX < enemyX + 10 and bulletY > enemyY - 10 and bulletY < enemyY + 10) :
				self.enemy.hideturtle()

	# Defining screen window
	def createWindow(self) :
		# Create window
		self.window = turtle.Screen()
		self.window.bgcolor("black")
		self.window.title("Space Invaders v1.0 by Thiago Pereira")

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

	# Defining and positioning player
	def createPlayer(self) :
		# Draw player
		self.player = turtle.Turtle()
		self.player.color("blue")
		self.player.shape("triangle")
		self.player.penup()
		self.player.speed(0)

		# Player initial position
		self.player.setposition(0, -270 + 40)
		self.player.setheading(90)

	# Defining and positioning player bullet
	def createPlayerBullet(self) :
		# Draw player bullet
		self.bullet = turtle.Turtle()
		self.bullet.color("yellow")
		self.bullet.shape("triangle")
		self.bullet.penup()
		self.bullet.speed(0)

		# Bullet initial position
		self.bullet.setposition(0, 0)
		self.bullet.setheading(90)
		self.bullet.shapesize(0.5, 0.5)
		self.bullet.hideturtle()

	# Defining and positioning enemy
	def createEnemy(self) :
		# Draw enemy
		self.enemy = turtle.Turtle()
		self.enemy.color("red")
		self.enemy.shape("circle")
		self.enemy.penup()
		self.enemy.speed(0)

		# Enemy initial position
		self.enemy.setposition(-270 + 40, 270 - 40)

	# Move spaceship left
	def moveLeft(self) :
		x = self.player.xcor()
		x -= self.playerSpeed

		if(x < -230) :
			x = -230

		self.player.setx(x)

	# Move spaceship right
	def moveRight(self) :
		x = self.player.xcor()
		x += self.playerSpeed

		if(x > 230) :
			x = 230

		self.player.setx(x)

	# Spaceship gun
	def fireBullet(self) :
		if(self.bulletState == "ready") :
			self.bulletState = "fire"
			x = self.player.xcor()
			y = self.player.ycor() + 10
			self.bullet.setposition(x, y)
			self.bullet.showturtle()

def main() :
	game = SpaceInvaders()

if __name__ == "__main__" :
	main()