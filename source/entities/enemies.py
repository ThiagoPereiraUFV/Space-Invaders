import turtle
import random

class Enemies :
	# Drawing and positioning enemies
	def __init__(self, nEnemies, nEnemiesR, color, level, dimension):
		self.enemies = []
		row = 1
		col = 0

		for i in range(nEnemies) :
			if(i == row*5) :
				row += 1
				col = 0
			
			enemy = turtle.Turtle()
			enemy.hideturtle()
			colorIndex = random.randint(0, len(color)-1)
			enemy.color(color[colorIndex])
			enemy.shape("circle")
			enemy.penup()
			enemy.speed(0)
			enemy.setposition(-(dimension/2) + 40 + col*(dimension/nEnemiesR), (dimension/2) - 40*row)
			enemy.showturtle()

			self.enemies.append(enemy)
			col += 1

		# Setting enemies speed
		self.speed = 2*dimension*0.003 + level*0.5

	# Get enemies
	def __getitem__(self, index) :
		if(index >= len(self.enemies)) :
			raise IndexError("End")
		else :
			return self.enemies[index]