import turtle

class Player :
	# Drawing and positioning player and bullet
	def __init__(self, dimension) :
		# Window dimension
		self.dimension = dimension

		# Draw player
		self.player = None
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

		# Bullet state
		self.bulletState = "ready"

		# Setting player and bullet speed
		self.playerSpeed = 15*self.dimension*0.001
		self.bulletSpeed = 20*self.dimension*0.003

	# Move player left
	def moveLeft(self) :
		x = self.player.xcor()
		x -= self.playerSpeed

		if(x < -(self.dimension/2) + 40) :
			x = -(self.dimension/2) + 40

		self.player.setx(x)

	# Move player right
	def moveRight(self) :
		x = self.player.xcor()
		x += self.playerSpeed

		if(x > (self.dimension/2) - 40) :
			x = (self.dimension/2) - 40

		self.player.setx(x)

	# Player gun
	def fireBullet(self) :
		if(self.bulletState == "ready") :
			self.bulletState = "fire"
			self.bullet.setposition(self.player.xcor(), self.player.ycor() + 10)
			self.bullet.showturtle()