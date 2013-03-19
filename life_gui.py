import Tkinter as tk
import life_game as lg
import time

class GameBoard(tk.Frame):
	def __init__(self, parent, rows=10, columns=10, size=32, color1="black", color2="green"):
		'''size is the size of a square, in pixels'''
		self.rows = rows
		self.columns = columns
		self.size = size
		self.color1 = color1
		self.color2 = color2

		canvas_width = columns * size
		canvas_height = rows * size

		tk.Frame.__init__(self, parent)
		self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
		                        width=canvas_width, height=canvas_height, background="bisque")
		self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
		self.go = tk.Button(self, text="Go", command=self.draw)
        
        # this binding will cause a refresh if the user interactively
        # changes the window size
        #self.canvas.bind("<Configure>", self.refresh)

	def draw(self, life_grid):
		

		for row in range(self.rows):
			for col in range(self.columns):
				x1 = (col * self.size)
				y1 = (row * self.size)
				x2 = x1 + self.size
				y2 = y1 + self.size
				if life_grid.grid[row][col] == 0:
					color="black"
				else:
					color="green"
		self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
		#color = self.color1 if color == self.color2 else self.color2
		#life_grid.update()
		#self.after(4000, self.draw(life_grid))
	
	def change_color(self, life_grid):
		for row in range(self.rows):
		#color = self.color1 if color == self.color2 else self.color2
			for col in range(self.columns):
				if life_grid.grid[row][col] == 0:
					color="black"
				else:
					color="green"
				self.canvas.update(fill=color)






if __name__ == "__main__":
    

	life_grid=lg.Board(10,1,0.6)
	root = tk.Tk()

	board = GameBoard(root)

	board.draw(life_grid)
	life_grid.update()
	board.change_color(life_grid)
	board.pack(side="top", fill="both", expand="true", padx=4, pady=4)

	# life_grid.update()
	# board.draw(life_grid)

	# board.pack(side="top", fill="both", expand="true", padx=4, pady=4)

	# C = Tkinter.Canvas(top, bg="green", height=320, width=320)

	# thing = lg.Board(10,1,.6)
	# # count=10
	# # while(count>0):
	# # 	Draw(C, thing)
	# # 	C.pack()
	# # 	thing.update()
	# # 	count= count-1
	
	# frame= Frame(top, width=350, height=350)

	# Draw(C, thing)
	# C.bind("<Key>", key)
	# C.pack()
	print "WOOHOO"


	root.mainloop()
