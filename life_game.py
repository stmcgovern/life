#reproduce Conway's game of Life
#have a nxn board (say n=10), each cell can be 0 or 1 (dead or alive)
#-> seed the board in some way (e.g. random , determinate patterns, etc.)
#->update function which follows the set of rules
#---rules:(from wikipedia.org)
#-----1.Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#-----2.Any live cell with two or three live neighbours lives on to the next generation.
#-----3.Any live cell with more than three live neighbours dies, as if by overcrowding.
#-----4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#update is applied uniformly to the board at one time step.

#strategy: nxn array, "current", and a copy of it. update function is applied to each cell of current board and the copy is modified to reflect the "tick", ie the time step

import numpy as np
import random as r

n_size =10

#initialize the grid / all 0s
def init(n_size):
	#n_size=10
	grid = np.zeros(shape=(n_size,n_size),dtype=np.int)
	return grid

#turn  a number <grains> of  cells to be alive, randomly chosen
def seed(grid, grains):
	for x in xrange(grains):
		row=r.randint(1,8)
		col=r.randint(1,8)
		grid[row][col]=1

#for each cell in the grid, the 4 rules (As above) are applied in order

#def neighbors(grid, live):
#	for cell in live:




#SKETCH
# def Update(grid): # takes in current grid and returns an updated one
# 	live=get_live(grid)
# 	
	#for item in live:
# 		neighbors=get_neighbors(item)
# 		alive_neighbors=get_alive_neighbors(neighbors, grid)
# 		if alive_neighbors == case 1:
# 			next_grid[item]=1 or 0

def get_live(grid):
	live=[]
	for row in xrange(n_size):
		for col in xrange(n_size):
			#print cell
			cell=grid[row][col]
		
			if cell ==1:
				live.append((row,col))
	return live

def get_neighbors(grid, cell):
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

def sum_neighbors(grid, neighbors):
	alive_neighbors=0
	for index1 in xrange(len(neighbors)):
		i=neighbors[index1][0]
		j=neighbors[index1][1]

		#print "i,j", i,j
		#print "grid_value", grid[i][j]
		alive_neighbors = alive_neighbors +grid[i][j]

	#print "alive_neighbors", alive_neighbors
	return alive_neighbors

def evolution(alive_neighbors): #return 0 or 1 based on rules
	if alive_neighbors<2:
		return 0
	elif alive_neighbors == 2 or alive_neighbors== 3:
		return 1
	elif alive_neighbors>3:
		return 0


def Update(grid):
	next_grid=init(n_size)
	#first get live cells
	live = get_live(grid)
	for cell in live: 
		neighbors = get_neighbors(grid, cell)
		alive_neighbors=sum_neighbors(grid, neighbors)
		i,j=cell
		next_grid[i][j]=evolution(alive_neighbors)

	#do something about 4th rule

	return next_grid




def main(n_size, time_steps):

	grid=init(n_size)
	seed(grid, 40)
	print grid

	for i in xrange(time_steps):
		next_grid=Update(grid)
		print next_grid

		
	print "Game OVER"







# 	#generate a list of neighbors for each live cell with index i,j
	
	
# 	for index in xrange(len(live)): #for eache cell with value 1
# 		neighbors=[]
# 		i,j=live[index]
# 		#print "i,j", i,j
# 		neighbors.append([(i-1,j-1),(i-1,j), (i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1), (i+1,j),(i+1,j+1)])
# 		#print "index", index
# 		#print "cell", live[index]
# 		#print "neighbors", neighbors

# 		#get the number of alive 
# 		alive_neighbors=0
# 		for index1 in xrange(len(neighbors)):
# 			i=neighbors[0][index1][0]
# 			j=neighbors[0][index1][1]

# 			#print "i,j", i,j
# 			#print "grid_value", grid[i][j]
# 			alive_neighbors = alive_neighbors +grid[i][j]

# 		print "alive_neighbors", alive_neighbors
# 		#check the rules against the neighbors
# 		i,j=live[index]
# 		print "i,j end", i,j
# 		if alive_neighbors<2:
# 			next_grid[i][j]=0
# 		elif alive_neighbors == 2 or alive_neighbors== 3:
# 			next_grid[i][j]=1
# 		elif alive_neighbors>3:
# 			next_grid[i][j]=0
	
# 	print next_grid
# 	return next_grid



# 	#copy the update cell to next_grid




# grid =init(n_size)

# seed(grid, 40)
# print grid

# next_grid=Update(grid)

# print next_grid


