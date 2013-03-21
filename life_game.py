#reproduce Conway's game of Life

from random import randint
from pprint import pprint
import sys
import pdb
import numpy as np


#command line argument getting
print sys.argv

if len(sys.argv)==5:

	n_size=int(sys.argv[1])
	time_steps=int(sys.argv[2])
	initial_density =float(sys.argv[3])
	initial_jump = int(sys.argv[4])
else:
	n_size =10
	time_steps=10
	initial_density = 0.4
	initial_jump = 100



class Board(object):
	def __init__(self, size, time_steps, initial_density, initial_jump):
		self.size=size
		self.time_steps=time_steps
		self.initial_density =initial_density
		self.initial_jump = initial_jump
 		
 		self.grid = np.zeros(shape=(self.size,self.size),dtype=int)
 		
 		self.next_grid = np.zeros(shape=(self.size,self.size),dtype=int)
 		#self.next_grid = [[0 for i in range(self.size)] for j in range(self.size)]
 		#self.grid = [[0 for i in range(self.size)] for j in range(self.size)]

 		#pprint(self.grid)
 		grains=int(self.initial_density*(self.size*self.size))
		for x in xrange(grains):
			row=randint(0,self.size-1) 
			col=randint(0,self.size-1)
			self.grid[row][col]=1
			#pdb.set_trace()

		for x in xrange(self.initial_jump):
			self.update()
		print "ready to rock"



	def update(self):
	
		next=self.next_grid
		#just scan through the whole thing
		for row in xrange(self.size):
			for col in xrange(self.size):
				
				alive_neighbors = self.get_sum(row, col)
				
				if(self.grid[row][col]==0):
					next[row][col]=self.evolution_0(alive_neighbors)
				else:
					next[row][col]=self.evolution_1(alive_neighbors)
		
		self.grid=next
		
			# if(mutate==True):
			# #probability that a dead cell animates
			# 	if(randint(0,100)<50):
			# 		row=randint(0,self.size-1) 
			# 		col=randint(0,self.size-1)
			# 		self.grid[row][col]=1

		

	def get_sum(self, i, j):
		#wraps around if at the border
		far =self.size-1
		
		up=i-1
		down=i+1
		left=j-1
		right=j+1
		
		if(i==0):
			up=far
		if(i==far):
			down=0
		if(j==0):
			left=far
		if(j==far):
			right=0

		alive_neighbors=0
		
		alive_neighbors += self.grid[up][left]
		alive_neighbors += self.grid[up][j]
		alive_neighbors += self.grid[up][right]
		alive_neighbors += self.grid[i][left]
		alive_neighbors += self.grid[i][right]
		alive_neighbors += self.grid[down][left]
		alive_neighbors += self.grid[down][j]
		alive_neighbors += self.grid[down][right]


		return alive_neighbors


	def evolution_0(self, alive_neighbors): #return 0 or 1 based on rules for dead cell
		if  alive_neighbors== 3:
			return 1
		else:
			return 0

	def evolution_1(self,alive_neighbors): #return 0 or 1 based on rules for alive cell
		if alive_neighbors<2:
			return 0
		elif alive_neighbors <4:
			return 1
		else:
			return 0

	
	
	def display(self):
		pprint(self.grid)
	
	def go(self):
		self.update()
		#self.display()

def main():
	
	board=Board(n_size, time_steps, initial_density, initial_jump)

	pprint(board.grid)
	print "go!"
	for i in xrange(time_steps):
		board.update()
		pprint(board.grid)
		print "tick"


		
	print "Game OVER"





if __name__ == '__main__':
	main()


