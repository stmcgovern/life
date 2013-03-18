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
 		pprint(self.grid)
 		grains=int(self.initial_density*(self.size*self.size))
		for x in xrange(grains):
			row=randint(1,self.size-2) #leaves edges at 0 during seeding
			col=randint(1,self.size-2)
			self.grid[row][col]=1
			#pdb.set_trace()

	def update(self):

		next_grid=[[0 for i in range(self.size)] for j in range(self.size)]
	#just scan through the whole thing
		for row in xrange(1,self.size-1):
			for col in xrange(1,self.size-1):
				
				cell = (row,col)
				neighbors = self.get_neighbors(cell)
				alive_neighbors=self.sum_neighbors(neighbors)
				i,j=cell
				if(self.grid[i][j]==0):
					next_grid[i][j]=self.evolution_0(alive_neighbors)
				else:
					next_grid[i][j]=self.evolution_1(alive_neighbors)

		#pprint(next_grid)
		#print "kjldsfajklfdsaj;fad"
		self.grid=next_grid

	def get_neighbors(self, cell):
		neighbors=[]
		i,j=cell
		#print "i,j", i,j
		neighbors.append((i-1,j-1))
		neighbors.append((i-1,j))
		neighbors.append((i-1,j+1))
		neighbors.append((i,j-1))
		neighbors.append((i,j+1))
		neighbors.append((i+1,j-1))
		neighbors.append((i+1,j))
		neighbors.append((i+1,j+1))
		#print "index", index
		#print "cell", live[index]
		#print "neighbors", neighbors
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

	for i in xrange(time_steps):
		board.update()
		pprint(board.grid)

		
	print "Game OVER"





if __name__ == '__main__':
	main()


