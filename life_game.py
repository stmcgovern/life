#reproduce Conway's game of Life


import numpy as np
import random as r
#magic number of grid size
n_size =10
time_steps=10

#TODO 
#sort out the boundary cases. (e.g. wrap, permanent dead edges)
#integrate all 4 rules (now last one is ad hoc)- inefficient!
#have program run in interpreter, with command to time step incrementally


def main(time_steps):
	grid=init()
	seed(grid, 60)#magic number of initial alive cells
	print grid

	for i in xrange(time_steps):
		next_grid=Update(grid)
		print next_grid
		grid=next_grid

		
	print "Game OVER"




#initialize the grid / all 0s
def init():
	
	grid = np.zeros(shape=(n_size,n_size),dtype=np.int)
	return grid

#turn  a number <grains> of  cells to be alive, randomly chosen
def seed(grid, grains):
	for x in xrange(grains):
		row=r.randint(1,n_size-2) # ad hoc -leave edges dead during seeding
		col=r.randint(1,n_size-2)
		grid[row][col]=1


#SKETCH
# def Update(grid): # takes in current grid and returns next_grid
# 	live=get_live(grid)
# 	
	#for cell in live:
# 		neighbors=get_neighbors(grid, cell)
# 		alive_neighbors=sum_neighbors(neighbors, grid)
# 		evolution returns 0 or 1 to next_grid for the cell in question
#		

def Update(grid):

	next_grid=init()

	live = get_live(grid)

	for cell in live: 
		neighbors = get_neighbors(grid, cell)
		alive_neighbors=sum_neighbors(grid, neighbors)
		i,j=cell
		next_grid[i][j]=evolution(alive_neighbors)

	#implement the 4th rule, concerning dead cells with 3 alive neighbors
	for row in xrange(n_size):
		for col in xrange(n_size):
			
			status=grid[row][col]
			cell = (row,col)
			neighbors = get_neighbors(grid, cell)
			if cell ==1:
				pass #do rules 1-3
			elif cell==0:
				alive_neighbors = sum_neighbors(grid, neighbors)
				if alive_neighbors==3:
					next_grid[row][col]=1

	return next_grid



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









# RUNNING THE DARN THING

main(time_steps)







#SCRAP




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


