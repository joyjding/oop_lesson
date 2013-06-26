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
OPPO= None
MELEE = False
######################

GAME_WIDTH = 7
GAME_HEIGHT = 7

#### Put class definitions here ####
class Tree (GameElement):
	IMAGE = "Rock"
	SOLID = True

	def interact(self,player):
		player.health-=1
		GAME_BOARD.draw_msg("%s hit a bump! Minus 1 Health. Your current health is %d / 3!" % (player.name, player.health))

	def update(self,dt):
		if (PLAYER.x==6 and PLAYER.y==6) or (OPPO.x==6 and OPPO.y==6):
			GAME_BOARD.del_el(self.x, self.y)


class MovingTree(Tree):
	IMAGE="TallTree"
	SOLID=True

class Cw1_tree(MovingTree):

	def update(self,dt):
		if (PLAYER.x == 6 and PLAYER.y ==6) or (OPPO.x == 6 and OPPO.y ==6)  or MELEE==True:
			GAME_BOARD.del_el(self.x, self.y)
			return
		self.last_time+=dt
		if self.last_time<1 or self.x==6 or self.y==6 or MELEE==True :
			return
		if self.mark==0:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+1,self.y,self)
			self.last_time=0
			self.mark=1
		elif self.mark==1:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y+1,self)
			self.last_time=0	    	
			self.mark=2
		elif self.mark==2:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-1,self.y,self)
			self.last_time=0
			self.mark=3
		elif self.mark==3:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y-1,self)
			self.last_time=0	    	
			self.mark=0			
		
class Ccw2_tree(MovingTree):

	def update(self,dt):
		if (PLAYER.x == 6 and PLAYER.y ==6) or (OPPO.x == 6 and OPPO.y ==6)  or MELEE==True:
			GAME_BOARD.del_el(self.x, self.y)
			return

		self.last_time+=dt
		if self.last_time<1.5 or MELEE==True:
			return
		if self.mark==0:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-2,self.y,self)
			self.last_time=0
			self.mark=1
		elif self.mark==1:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y+2,self)
			self.last_time=0	    	
			self.mark=2
		elif self.mark==2:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+2,self.y,self)
			self.last_time=0
			self.mark=3
		elif self.mark==3:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y-2,self)
			self.last_time=0	    	
			self.mark=0			

class Zigzag_tree(MovingTree):
	
	def update(self,dt):
		if (PLAYER.x == 6 and PLAYER.y ==6) or (OPPO.x == 6 and OPPO.y ==6) or MELEE==True:
			return
		self.last_time+=dt
		if self.last_time<2 or MELEE==True:
			return
		if self.mark==0:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+1,self.y,self)
			self.last_time=0
			self.mark=1
		elif self.mark==1:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y+1,self)
			self.last_time=0	    	
			self.mark=2
		elif self.mark==2:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+1,self.y,self)
			self.last_time=0
			self.mark=3
		elif self.mark==3:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y+1,self)
			self.last_time=0	    	
			self.mark=4		
		elif self.mark==4:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x+1,self.y,self)
			self.last_time=0	    	
			self.mark=5	
		elif self.mark==5:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-1,self.y,self)
			self.last_time=0
			self.mark=6
		elif self.mark==6:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y-1,self)
			self.last_time=0	    	
			self.mark=7
		elif self.mark==7:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-1,self.y,self)
			self.last_time=0
			self.mark=8
		elif self.mark==8:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x,self.y-1,self)
			self.last_time=0	    	
			self.mark=9	
		elif self.mark==9:
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(self.x-1,self.y,self)
			self.last_time=0	    	
			self.mark=0		





class Character(GameElement):
	IMAGE = "Horns"
	SOLID = True

	def __init__(self):
		GameElement.__init__(self)
		self.totebag = []
		self.health = 3
		self.name = "Slayer"

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

	def update(self,dt):
		if self.health==0:
		
			GAME_BOARD.del_el(self.x,self.y)
			GAME_BOARD.set_el(1,0,self)
			GAME_BOARD.draw_msg("Slayer, you've lost all your health. Come back home!")
			self.health=3


class Opponent(Character):
	IMAGE = "Princess"
	SOLID=True

	def __init__(self):
		GameElement.__init__(self)
		self.totebag = []
		self.health = 3
		self.name = "Prancy"

	def text_next(self, op_direction):
		if op_direction == "up":
			return (self.x, self.y-1)
		elif op_direction == "down":
			return (self.x, self.y+1)
		elif op_direction == "left":
			return (self.x-1, self.y)
		elif op_direction == "right":
			return (self.x+1, self.y)
		return None

	def update(self,dt):
		if self.health==0:
		
			GAME_BOARD.del_el(self.x, self.y)
			GAME_BOARD.set_el(0,1,self)
			GAME_BOARD.draw_msg("Prancy, you've lost all your health! Come back home!")
			self.health=3


class Gem(GameElement):
	IMAGE ="BlueGem"
	SOLID = False

	def interact(self,player):
		player.totebag.append(self)
		
		GAME_BOARD.draw_msg("%s got a gem! You have %d items!" %(player.name, len(player.totebag)))
	def update(self,dt):
		gem_ppp=[(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),
		(6,0),(6,1),(6,2),(6,3),(6,4),(6,5)]
		winner = False
		if PLAYER.x == 6 and PLAYER.y ==6:
			winner=PLAYER.name
		if OPPO.x ==6 and OPPO.y==6:
			winner=OPPO.name
		if winner !=False:
			for i in range(6):
				for j in range(6):
					gem_ppp.append((i,j))
			for pos in gem_ppp:
				GAME_BOARD.set_el(pos[0],pos[1],self)
			GAME_BOARD.draw_msg("%s, you win! Here's 25 more gems!" %winner)


class Finish_block(GameElement):
	IMAGE = "Chest"
	SOLID = False

class Key(GameElement):
	IMAGE = "Key"
	SOLID = False

	def interact(self,player):
		global MELEE
		MELEE=True
		GAME_BOARD.wipe()
		GAME_BOARD.draw_msg("Choose your next adventure by picking a door.")		
		
	def update(self,dt):
		winner = False
		if PLAYER.x == 6 and PLAYER.y ==6:
			winner=PLAYER.name
		if OPPO.x ==6 and OPPO.y==6:
			winner=OPPO.name
		if winner !=False:
			GAME_BOARD.set_el(2,5,self)

class DeathChest(GameElement):
	IMAGE = "DoorClosed"
	SOLID = False
	
	def interact(self,player):
		GAME_BOARD.draw_msg("You picked the wrong door. You're eaten by disarray!")

	def update(self,dt):
		if MELEE==True:
			GAME_BOARD.set_el(3,3,self)
			GAME_BOARD.set_el(4,3,self)

class LiveChest(GameElement):
	IMAGE = "DoorClosed"
	SOLID = False
	
	def interact(self,player):	
		GAME_BOARD.draw_msg("You picked the right door. YOU WIN!")

	def update(self,dt):
		if MELEE==True:
			GAME_BOARD.set_el(2,3,self)

# class DeathChest(GameElement):
# 	IMAGE = "Chest"
# 	SOLID = False
# 	GAME_BOARD.draw_msg("You picked the wrong chest. You're dead!")


####   End class definitions    ####
def keyboard_handler():

	direction = None
	op_direction=None

	if KEYBOARD[key.UP] and PLAYER.y!=0:
		direction="up"
	elif KEYBOARD[key.DOWN] and PLAYER.y!=6:        
		direction="down"
	elif KEYBOARD[key.RIGHT] and PLAYER.x!=6:       
		direction="right"
	elif KEYBOARD[key.LEFT] and PLAYER.x!=0:                
		direction="left"

	elif KEYBOARD[key.W] and OPPO.y!=0:
		op_direction="up"
	elif KEYBOARD[key.S] and OPPO.y!=6:        
		op_direction="down"
	elif KEYBOARD[key.D] and OPPO.x!=6:       
		op_direction="right"
	elif KEYBOARD[key.A] and OPPO.x!=0:                
		op_direction="left"		


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

	if op_direction:
		next_location = OPPO.text_next(op_direction)
		next_x = next_location[0]
		next_y = next_location[1]
		existing_el=GAME_BOARD.get_el(next_x,next_y)
		if existing_el:
			existing_el.interact(OPPO)
		if existing_el is None or not existing_el.SOLID:
			GAME_BOARD.del_el(OPPO.x, OPPO.y)
			GAME_BOARD.set_el(next_x,next_y,OPPO)  

def initialize():  

	global PLAYER
	PLAYER=Character()
	GAME_BOARD.register(PLAYER)
	GAME_BOARD.set_el(1,0,PLAYER)

	global OPPO
	OPPO=Opponent()
	GAME_BOARD.register(OPPO)
	GAME_BOARD.set_el(0,1,OPPO)	
	
	cwtrees_position=[(0,3),(4,1),(3,0),(5,2)]
	cwtrees=[]
	for pos in cwtrees_position:
		cw_tree=Cw1_tree()
		GAME_BOARD.register(cw_tree)
		GAME_BOARD.set_el(pos[0],pos[1],cw_tree)
		cwtrees.append(cw_tree)

	trees_position=[(6,1),(3,3),(2,6),(1,1),(2,1),(1,2),(0,6),(0,5),(5,5)]
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
	
	gems=[]
	gem_positions=[(0,2),(0,3),(0,4),
	(3,2),(4,2),(5,2),(2,0),
	(0,3),(1,3),(2,3),(4,3),(5,3),(6,3),
	(0,4),(1,4),(2,4),(3,4),
	(4,5),(6,5),
	(1,6),(3,6),(6,6)]
	for pos in gem_positions:
		gem=Gem()
		GAME_BOARD.register(gem)
		GAME_BOARD.set_el(pos[0],pos[1],gem)
		gems.append(gem)	
	finish = Finish_block()
	GAME_BOARD.register(finish)
	GAME_BOARD.set_el(6,6, finish)

	key=Key()
	GAME_BOARD.register(key)
	GAME_BOARD.draw_msg("Ascertain the treasure chest!")
	
	live_chest=LiveChest()
	GAME_BOARD.register(live_chest)

	death_chest=DeathChest()
	GAME_BOARD.register(death_chest)
	# 	global PLAYER
	# 	PLAYER=Character()
	# 	GAME_BOARD2.register(PLAYER)
	# 	GAME_BOARD2.set_el(1,0,PLAYER)

	# 	global OPPO
	# 	OPPO=Opponent()
	# 	GAME_BOARD2.register(OPPO)
	# 	GAME_BOARD2.set_el(0,1,OPPO)	
		
	# 	GAME_BOARD2.draw_msg("You're in a new place now! Fight Fight Fight Fight!")
