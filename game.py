import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 7
GAME_HEIGHT = 7

#### Put class definitions here ####
class Tree (GameElement):
	IMAGE = "ShortTree"
	SOLID = True

class Cw1_tree(GameElement):
	IMAGE = "TallTree"
	SOLID = True

	def update(self,dt):
		if PLAYER.x == 6 and PLAYER.y ==6:
			return

		self.last_time+=dt
		if self.last_time<1 or self.x==6 or self.y==6:
			return
		if self.mark==0:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+1,self.y,self)
			print self.x, self.y
			self.last_time=0
			self.mark=1
		elif self.mark==1:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y+1,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=2
		elif self.mark==2:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-1,self.y,self)
			print self.x, self.y
			self.last_time=0
			self.mark=3
		elif self.mark==3:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y-1,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=0			
		
class Ccw2_tree(GameElement):
	IMAGE = "TallTree"
	SOLID = True

	def update(self,dt):
		if PLAYER.x == 6 and PLAYER.y ==6:
			return

		self.last_time+=dt
		if self.last_time<1.5:
			return
		if self.mark==0:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-2,self.y,self)
			print self.x, self.y
			self.last_time=0
			self.mark=1
		elif self.mark==1:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y+2,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=2
		elif self.mark==2:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+2,self.y,self)
			print self.x, self.y
			self.last_time=0
			self.mark=3
		elif self.mark==3:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y-2,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=0			

class Zigzag_tree(GameElement):
	IMAGE = "TallTree"
	SOLID = True

	def update(self,dt):
		if PLAYER.x == 6 and PLAYER.y ==6:
			return
		self.last_time+=dt
		if self.last_time<2:
			return
		if self.mark==0:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+1,self.y,self)
			print self.x, self.y
			self.last_time=0
			self.mark=1
		elif self.mark==1:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y+1,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=2
		elif self.mark==2:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+1,self.y,self)
			print self.x, self.y
			self.last_time=0
			self.mark=3
		elif self.mark==3:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y+1,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=4		
		elif self.mark==4:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+1,self.y,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=5	
		elif self.mark==5:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-1,self.y,self)
			print self.x, self.y
			self.last_time=0
			self.mark=6
		elif self.mark==6:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y-1,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=7
		elif self.mark==7:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-1,self.y,self)
			print self.x, self.y
			self.last_time=0
			self.mark=8
		elif self.mark==8:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y-1,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=9	
		elif self.mark==9:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-1,self.y,self)
			print self.x, self.y
			self.last_time=0	    	
			self.mark=0		


class Character(GameElement):
	IMAGE="Horns"
	def __init__(self):
		GameElement.__init__(self)
		self.totebag = []

	def text_next(self, direction):
		if direction == "up":
			return (self.x, self.y-1)
		elif direction == "down":
			return (self.x, self.y+1)
		elif direction == "left":
			return (self.x-1, self.y)
		elif direction == "right":
			return (self.x+1, self.y)
		return None

class Gem(GameElement):
	IMAGE ="BlueGem"
	SOLID = False

	def interact(self,player):
		player.totebag.append(self)
		GAME_BOARD.draw_msg("Capture the gems before the trees crush them! You have %d items!" %(len(player.totebag)))
	def update(self,dt):
		if PLAYER.x == 6 and PLAYER.y ==6:
			for i in range(6):
				for j in range(6):
					GAME_BOARD.set_el(i,j,self)
			GAME_BOARD.draw_msg("You win! Capture the gems!.")    

class Finish_block(GameElement):
	IMAGE = "Chest"
	SOLID = False

####   End class definitions    ####
def keyboard_handler():

	direction = None

	if KEYBOARD[key.UP] and PLAYER.y!=0:
		direction="up"
	elif KEYBOARD[key.DOWN] and PLAYER.y!=6:        
		direction="down"
	elif KEYBOARD[key.RIGHT] and PLAYER.x!=6:       
		direction="right"
	elif KEYBOARD[key.LEFT] and PLAYER.x!=0:                
		direction="left"

	if direction:
		next_location = PLAYER.text_next(direction)
		next_x = next_location[0]
		next_y = next_location[1]
		existing_el=GAME_BOARD.get_el(next_x,next_y)
		if existing_el:
			existing_el.interact(PLAYER)
		if existing_el is None or not existing_el.SOLID:
			GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
			GAME_BOARD.set_el(next_x,next_y,PLAYER)   	

def initialize():  
	global PLAYER
	PLAYER=Character()
	GAME_BOARD.register(PLAYER)
	GAME_BOARD.set_el(0,0,PLAYER)
	print PLAYER.x, PLAYER.y,"this is the player's position"
	
	cwtrees_position=[(0,3),(4,1),(3,0),(5,2)]
	cwtrees=[]
	for pos in cwtrees_position:
		cw_tree=Cw1_tree()
		GAME_BOARD.register(cw_tree)
		GAME_BOARD.set_el(pos[0],pos[1],cw_tree)
		cwtrees.append(cw_tree)

	trees_position=[(6,1),(3,3),(2,6),(2,5),(1,1),(2,1),(1,0),(0,6),(0,5),(5,5)]
	trees=[]
	for pos in trees_position:
		tree=Tree()
		GAME_BOARD.register(tree)
		GAME_BOARD.set_el(pos[0],pos[1],tree)
		trees.append(tree)

	exit_tree =Ccw2_tree()
	GAME_BOARD.register(exit_tree)
	GAME_BOARD.set_el(6, 3, exit_tree)

	ziggy = Zigzag_tree()
	GAME_BOARD.register(ziggy)
	GAME_BOARD.set_el(1,3, ziggy)
	
	gem = Gem()	
	GAME_BOARD.register(gem)

	finish = Finish_block()
	GAME_BOARD.register(finish)
	GAME_BOARD.set_el(6,6, finish)
	
	GAME_BOARD.draw_msg("Ascertain the treasure chest!")      
		


		