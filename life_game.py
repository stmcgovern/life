#Conway's game of Life simulation

#things to add:
# world connectivity: wrap OR fall off edge(DEAD_BORDERS=True), or arbitrary cell "neighbors"
# population count: track population stability
# SEEDING: add configurations of cells rather than random seed
# zoo: create a pen to contain a number of cells (a box of permanently dead cells)
# 		place configurations of cells (animal) in a pen 


from random import randint
from pprint import pprint
import sys
import pdb
import numpy as np


class Board(object):
	def __init__(self, size, initial_density, grid_file, wrap):
		self.size=size
		self.wrap=wrap


 		if grid_file:
			self.grid=self.build_from_file(grid_file)
		elif initial_density is not None:
			self.grid=self.build_rand(initial_density)


		print "ready to rock"

	def build_rand(self, initial_density):
		grid= np.zeros(shape=(self.size,self.size),dtype=int)
		grains=int(initial_density*(self.size*self.size))
		for x in xrange(grains):
				
				row=randint(0,self.size-1) 
				col=randint(0,self.size-1)
				while (grid[row][col]==1):
					row=randint(0,self.size-1) 
					col=randint(0,self.size-1)
					
				grid[row][col]=1

		return grid

	def build_from_file(self, grid_file):
		grid= np.zeros(shape=(self.size,self.size),dtype=int)

		with file(grid_file, 'r') as f:
			for i,line in enumerate(f):
				stripped_line= line.strip()
				for j,char in enumerate(stripped_line):
					grid[i][j]=char

		return grid


	def update(self):
	
		next=np.zeros(shape=(self.size,self.size),dtype=int)
		#just scan through the whole thing
		for row in xrange(self.size):
			for col in xrange(self.size):
				
				if self.wrap==1:
					alive_neighbors = self.get_sum_wrap(row, col)
				else:
					alive_neighbors = self.get_sum_no_wrap(row, col)
					
				if(self.grid[row][col]==0):
				
					next[row][col]=self.evolution_0(alive_neighbors)
				else:
					next[row][col]=self.evolution_1(alive_neighbors)
		#pdb.set_trace()

		self.grid=next
		
			# if(mutate==True):
			# #probability that a dead cell animates
			# 	if(randint(0,100)<50):
			# 		row=randint(0,self.size-1) 
			# 		col=randint(0,self.size-1)
			# 		self.grid[row][col]=1
	
	def get_sum_no_wrap(self, i, j):
		#edge cells have fewer neighbors
		far =self.size-1
		
		up=i-1
		down=i+1
		left=j-1
		right=j+1
		

		alive_neighbors=0
		
		if(up >= 0 and left >= 0):
			alive_neighbors += self.grid[up][left]
		if(up >= 0):
			alive_neighbors += self.grid[up][j]
		if(up >= 0 and right <= far):
			alive_neighbors += self.grid[up][right]
		if(left >= 0):
			alive_neighbors += self.grid[i][left]
		if(right <= far):		
			alive_neighbors += self.grid[i][right]
		if(down <= far and left >= 0):		
			alive_neighbors += self.grid[down][left]
		if(down <= far):			
			alive_neighbors += self.grid[down][j]
		if(down <= far and right <= far):		
			alive_neighbors += self.grid[down][right]


		return alive_neighbors

	def get_sum_wrap(self, i, j):
		
		#wraps around if at the border
		#all cells have 8 neighbors
		far =self.size-1
		
		up=i-1
		down=i+1
		left=j-1
		right=j+1
		
		if(i==0):
			up=far
		elif(i==far):
			down=0
		
		if(j==0):
			left=far
		elif(j==far):
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
		elif alive_neighbors ==2 or alive_neighbors ==3:
			return 1
		else:
			return 0

	def pop_stats(self):
		pass
		# stats="log.txt"
		# with file(stats, 'w') as f:
		# 	for 
	
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
	main()


