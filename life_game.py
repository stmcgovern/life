#reproduce Conway's game of Life

from random import randint
from pprint import pprint
import sys
import pdb


#command line argument getting
print sys.argv

if len(sys.argv)==4:

	n_size=int(sys.argv[1])
	time_steps=int(sys.argv[2])
	initial_density =float(sys.argv[3])
else:
	n_size =10
	time_steps=10
	initial_density = 0.4



class Board(object):
	def __init__(self, size, attr2, attr3):
		self.size=size
		self.time_steps=attr2
		self.initial_density =attr3
 		
 		#self.grid = [[0]*size]*size#np.zeros(shape=(n_size,n_size),dtype=np.int)
 		self.grid = [[0 for i in range(self.size)] for j in range(self.size)]
 		#pprint(self.grid)
 		grains=int(self.initial_density*(self.size*self.size))
		for x in xrange(grains):
			row=randint(0,self.size-1) 
			col=randint(0,self.size-1)
			self.grid[row][col]=1
			#pdb.set_trace()



	def update(self):

		next_grid=[[0 for i in range(self.size)] for j in range(self.size)]
	
		#just scan through the whole thing
		for row in xrange(self.size):
			for col in xrange(self.size):
				
				cell = (row,col)
				neighbors = self.get_neighbors(cell)
				alive_neighbors=self.sum_neighbors(neighbors)
				
				if(self.grid[row][col]==0):
					next_grid[row][col]=self.evolution_0(alive_neighbors)
				else:
					next_grid[row][col]=self.evolution_1(alive_neighbors)

		self.grid=next_grid

	def get_neighbors(self, cell):
		#wraps around if at the border
		far =self.size-1
		neighbors=[]
		i,j=cell
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

		neighbors.append((up,left))
		neighbors.append((up,j))
		neighbors.append((up,right))
		neighbors.append((i,left))
		neighbors.append((i,right))
		neighbors.append((down,left))
		neighbors.append((down,j))
		neighbors.append((down,right))

		return neighbors

	def sum_neighbors(self, neighbors):
		alive_neighbors=0
		for neighbor in neighbors:
			i, j = neighbor
			#print "i,j", i,j
			#print "grid_value", grid[i][j]
			alive_neighbors += self.grid[i][j]

		# print "alive_neighbors", alive_neighbors
		#assert alive_neighbors == sum(self.grid[i][j] for i, j in neighbors)
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



def main():
	
	board=Board(n_size, time_steps, initial_density)

	pprint(board.grid)
	print "go!"
	for i in xrange(time_steps):
		board.update()
		pprint(board.grid)
		print "tick"

		
	print "Game OVER"





if __name__ == '__main__':
	main()


