import life_game as lg
import sys
from pprint import pprint
import time

if len(sys.argv)==4:

	n_size=int(sys.argv[1])
	time_steps=int(sys.argv[2])
	initial_density =float(sys.argv[3])
else:
	n_size =10
	time_steps=10
	initial_density = 0.4



def main():
	
	board=lg.Board(n_size, time_steps, initial_density)
	start=time.time()

	for i in xrange(time_steps):
		board.update()
	
	end=time.time()
	duration=end-start
	print duration


if __name__ == '__main__':
	main()


