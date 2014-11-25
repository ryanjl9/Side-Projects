import random
#Main Class
class Board():
	def __init__(self, size, playerStartPos = False):
		self.playerStartPos = playerStartPos
		self.sizeX,self.sizeY = size.split(':')
		self.board_shell = self.generate()
		self.playerStart()
	#Generated the board
	def generate(self):
		yAxis = []
		for x in range(int(self.sizeY)):
			xAxis = []
			x = 0
			for y in range(int(self.sizeX)):
				xAxis.append(str(x+1))
				x+=1
			yAxis.append(xAxis)
		return yAxis
	#Searches coordinates for what is in the location
	def search(self, coords, p = False):
		xCoord,yCoord = coords.split(':')
		for x in range(0,len(self.board_shell)):
			if x == int(yCoord) - 1:
				if p == True:	#Debug
					print self.board_shell[x][int(xCoord)-1]
				else:
					return self.board_shell[x][int(xCoord)-1]
	#Changes what is at a certain coordinate
	def change(self, coords, value):
		xCoord,yCoord = coords.split(':')	
		self.board_shell[int(yCoord)-1][int(xCoord)-1] = value				
	#Renders the board
	def render(self):
		for x in self.board_shell:
			placeHolder = " "
			print placeHolder.join(x)
	#Puts the player in a certain starting position/random location
	def playerStart(self):
		if self.playerStartPos == False:
			xValue = random.randint(0,int(self.sizeX)-1)
			yValue = random.randint(0,int(self.sizeY)-1)
			self.change(str(yValue) +':'+ str(xValue), '@')
		elif type(self.playerStartPos) == str:
			self.change(self.playerStartPos, '@')
	#Gets the coordinates for anything with the same value
	def getCoords(self, value, p = False):
		for y in range(len(self.board_shell)):
			for x in range(len(self.board_shell[y])):
				if self.board_shell[y][x] == value:
					if p == True:	#Debug
						print '%s:%s'%(x+1,y+1)
					else:
						return '%s:%s'%(x+1,y+1)
	#Changes where something is by a certain direction
	def direction(self, direct):
		if direct == 'w' and self.movement('w'):
			currentCoords = self.getCoords('@')
			xCoord,yCoord = currentCoords.split(':')
			oldYCoord = yCoord
			yCoord = int(yCoord)-1
			self.change(xCoord +':'+ str(yCoord), '@')
			self.change(xCoord +':'+ oldYCoord, xCoord)
		elif direct == 's' and self.movement('s'):
			currentCoords = self.getCoords('@')
			xCoord,yCoord = currentCoords.split(':')
			oldYCoord = yCoord
			yCoord = int(yCoord)+1
			self.change(xCoord +':'+ str(yCoord), '@')
			self.change(xCoord +':'+ oldYCoord, xCoord)
		elif direct == 'a' and self.movement('a'):
			currentCoords = self.getCoords('@')
			xCoord,yCoord = currentCoords.split(':')
			oldXCoord = xCoord
			xCoord = int(xCoord)-1
			self.change(str(xCoord) +':'+ yCoord, '@')
			self.change(oldXCoord +':'+ yCoord, oldXCoord)
		elif direct == 'd' and self.movement('d'):
			currentCoords = self.getCoords('@')
			xCoord,yCoord = currentCoords.split(':')
			oldXCoord = xCoord
			xCoord = int(xCoord)+1
			self.change(str(xCoord) +':'+ yCoord, '@')
			self.change(oldXCoord +':'+ yCoord, oldXCoord)
		else:
			return False
	#Checks if player is at an edge
	def movement(self, direction):
		xCoord,yCoord = self.getCoords('@').split(':')
		if direction == 'w' and yCoord == '1':
			return False
		elif direction == 's' and yCoord == self.sizeY:
			return False
		elif direction == 'a' and xCoord == '1':
			return False
		elif direction == 'd' and xCoord == self.sizeX:
			return False
		else:
			return True			
#Defines board		
board = Board(size = '20:20', playerStartPos = '5:5')
#board.getCoords('@')
#board.search('1:1')
loop = True
board.render()
while(loop):
	direction = raw_input('Which direction do you want to move (wasd) > ')
	if direction[0] == '!': #Debug Stuff
		command = compile(direction[1:len(direction)], '<string>', 'exec')
		exec command
	elif direction != 'close': #If close isn't passed, player moves and board is re-rendered
		board.direction(direction)
		board.render()
	else:
		loop = False


		
	






