#visual representation for 10x10 life board
import life_game as lg
import Tkinter as tk
import sys
import argparse
import pdb

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='optionally, an input file', default=None)
parser.add_argument('--size', help='length of a side of the board', default=100)
parser.add_argument('--rand_dens', help='Initialize board randomly with --rand_dens <density>', type=float)

args = parser.parse_args()
print args

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=args.size, columns=args.size, size=5, color1="black", color2="green", grid_file=None):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.parent = parent
        self.running = True
        
        self.square_list = []

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)


        self.life = lg.Board(args.size, args.rand_dens, args.file)
        self.draw()
        self.next()


    def draw(self):
        
        '''Redraw the board, possibly in response to window being resized'''
        print "Drawing board"

        self.canvas.delete("square")
        color = self.color2
        for row in xrange(self.rows):
            grid_row = []
            for col in xrange(self.columns):
                x1 = col * self.size
                y1 = row * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size
                
                square_id=self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                grid_row.append(square_id)
            self.square_list.append(grid_row)

        
    def next(self):
        print "next firing, self.running is", self.running
        if self.running:
            self.life.update()
                
            for row in xrange(self.rows):
                for col in xrange(self.columns):
                    square_id = self.square_list[row][col]
                    if self.life.grid[row][col]==1:
                        color="green"
                    else:
                        color="black"

                    self.canvas.itemconfig(square_id, fill=color)
        self.parent.after(100, self.next)

    def pause_or_restart(self, event):
        self.running = not self.running

if __name__ == "__main__":
   
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    board.canvas.bind('<Button-1>', board.pause_or_restart)
    root.mainloop()
   
	
