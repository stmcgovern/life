life simulation
====

to run:
python life_gui.py [board size, int n] [ time_steps, int t] [initial density float 0-1] [initial jump, int jump]

board size nxn cells
time_steps is how many times to update (tick)
initial density gives fraction of alive cells, "random" distribution
initial jump is how many ticks update runs through upon initialization

e.g
python life_gui.py 50 1 0.4 100

note:time_steps at the moment is not used in click based progressions


====

Conway's game of life 

reproduce Conway's game of Life
have a nxn board (say n=10), each cell can be 0 or 1 (dead or alive)

-> seed the board in some way (e.g. random , determinate patterns, etc.)

->update function which follows the set of rules

---rules:(from wikipedia.org)

-----1.Any live cell with fewer than two live neighbours dies, as if caused by under-population.

-----2.Any live cell with two or three live neighbours lives on to the next generation.

-----3.Any live cell with more than three live neighbours dies, as if by overcrowding.

-----4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


update is applied uniformly to the board at one time step.