import life_game as lg
import sys
from pprint import pprint
import time

if len(sys.argv)==4:

	n_size=int(sys.argv[1])
	time_steps=int(sys.argv[2])
	initial_density =float(sys.argv[3])
	initial_jump = int(sys.argv[4])
else:
	n_size =10
	time_steps=10
	initial_density = 0.4
	initial_jump = 1



def time_test(n_size, time_steps):
	
	board=lg.Board(n_size, time_steps, initial_density, initial_jump)
	start=time.time()

	for i in xrange(time_steps):
		board.update()
	
	end=time.time()
	duration=end-start
	print duration
	#make a test log

def main():
	print "board size, time steps"
	for n in xrange(10,100,10):
		for t in xrange(1, 50, 10):
			print n,t
			time_test(n, t)

if __name__ == '__main__':
	main()


