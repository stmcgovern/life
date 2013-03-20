#visual representation for 10x10 life board
import life_game as lg
import Tkinter as tk
LENGTH=100
JUMP=100
class GameBoard(tk.Frame):
    def __init__(self, parent, rows=LENGTH, columns=LENGTH, size=12, color1="black", color2="green"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self .columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        
        self.list = []

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)


        self.life=lg.Board(LENGTH,1,0.6)
        self.life.go()
        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)


    def refresh(self, event):
        
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in xrange(self.rows):
            for col in xrange(self.columns):
                x1 =col * self.size
                y1 = row * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size
                
                square_id=self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                self.list.append(square_id)

        
    def next(self, event):
        for x in xrange(JUMP):
            self.life.update()
            
        count=0
        for row in xrange(self.rows):
            for col in xrange(self.columns):
                x=self.list[count]
                if self.life.grid[row][col]==1:
                    color="green"
                else:
                    color="black"

                self.canvas.itemconfig(x, fill=color)
            

                count=count+1



if __name__ == "__main__":
   
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    board.canvas.bind('<Button-1>', board.next)
    root.mainloop()
    


