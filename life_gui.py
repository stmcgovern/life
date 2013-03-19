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
		
		#self.go = tk.Button(self, text="Go", command=self.draw)
        
        # this binding will cause a refresh if the user interactively
        # changes the window size
		self.canvas.bind("<Button-1>", self.on_click())

	def on_click(self):
		pass
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
				box[row][col]=self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
		# life_grid.update()
		# self.after(4000, self.draw(life_grid))
		#color = self.color1 if color == self.color2 else self.color2
		#life_grid.update()
		#self.after(4000, self.draw(life_grid))
	
	# def change_color(self, life_grid):
		
		
	# 		self.canvas.tag.itemconfigure(fill="blue")

	# 	# for row in range(self.rows):
	# 	# #color = self.color1 if color == self.color2 else self.color2
	# 	# 	for col in range(self.columns):
	# 	# 		if life_grid.grid[row][col] == 0:
	# 	# 			color="black"
	# 	# 		else:
	# 	# 			color="green"
	# 	# 		self.canvas.update(fill=color)



if __name__ == "__main__":
    
	board = [ [None]*10 for _ in range(10) ]

	life=lg.Board(10,1,0.6)
	root = tk.Tk()
	life.update()
	

	root.mainloop()
