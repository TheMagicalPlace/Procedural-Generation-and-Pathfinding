from tkinter import *
from tkinter.ttk import *
from typing import List,Tuple,Iterable
import time
from twoDproceduralmaze import maze_generator
from itertools import chain
from AstarPathfinding import *
class CObjGenerator:
    generator = (i for i in range(100000))

class TKmazeplot:

    x = 1000
    y = 1000

    def __init__(self,mazex,mazey):
        master = Tk()
        self.canvas = Canvas(master,width=TKmazeplot.x,height=TKmazeplot.y)
        self.canvas.bind("<Button-1>", self.callback)
        self.scale = 1000//max(mazex,mazey)
        self.canvas.pack()
        self.canvas_objs = {}
        self.x,self.y = mazex,mazey
        self._setup_canvas_objs()
        self._setup_maze()
        master.mainloop()
    def _setup_canvas_objs(self):
        for x in range(0,self.x):
            for y in range(0,self.y):

                self.canvas_objs[(x,y)] = self.canvas.create_rectangle(x*self.scale,
                                                                       y*self.scale,
                                                                       (x+1)*self.scale,
                                                                       (y+1)*self.scale,
                                                                       fill='black')

        self.canvas.update()

    def _setup_maze(self):
        mgen = maze_generator(self.x-2,self.y-2)
        maze,hx,hy,start,end = mgen()
        self.canvas.itemconfigure(self.canvas_objs[start],fill='white')
        for x,y in zip(hx,hy):
            self.canvas.itemconfigure(self.canvas_objs[(x+1,y)],fill='white')
        self.canvas.update()
        print('y')
        self.pathfinder = Pathfinder(maze,(70,70),start,self)
        time.sleep(0.1)
        self.pathfinder()
    def show_path(self,x,y,color='blue'):

        for xx,yy in zip(x,y):
            self.canvas.itemconfigure(self.canvas_objs[(xx + 1, yy)], fill=color)
        self.canvas.update()
        time.sleep(0.01)
    def callback(self):
        pass


if __name__ == '__main__':
    obj = TKmazeplot(100,100)