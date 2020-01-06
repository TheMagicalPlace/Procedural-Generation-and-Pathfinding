


from matplotlib import pyplot as plt,colors
import matplotlib.animation
import numpy as np
import copy

from itertools import cycle
class liveplot:
    ''' animated plot generation for 2-dimensional plots'''
    def __init__(self,x_axis,y_axis,x=[],y=[]):
        self.plt = plt
        self.plt.ion()
        self.scatters = []
        self.fig, self.ax = plt.subplots()
        self.actpos = {}
        x = []
        y =  []
        self.c = []
        o = cycle(['black','white','yellow'])
        for i,_x in enumerate(range(x_axis)):
            for j,_y in enumerate(range(y_axis)):
                x.append([i,j])
                self.c.append([0,0,0])
                self.actpos[(i,j)] = len(x)-1
        cx = list(zip(*x))
        self.sc = self.ax.scatter(x=cx[0],y=cx[1],marker='s',c=self.c) # TODO give functionality to more than just scatter plots
        self.plt.draw()


        # Setting plot axis boundaries
        if isinstance(x_axis,int):
            plt.xlim(-1,x_axis+1)
        else:
            plt.xlim((x_axis[0]-1),(x_axis[1]+1))
        if isinstance(y_axis,int):
            plt.ylim((0-1),(y_axis+1))
        else:
            plt.ylim(y_axis[0],y_axis[1]+1)

    def animate_scatter(self,frames,color='g',marker='s'):
        if len(frames) == 2: frames = [frames]
        for a,b in frames:
            for aa,bb in zip(a,b):
                pos = self.actpos[(aa,bb)]
                self.c[pos] = colors.to_rgb(color)
        self.sc.set_facecolor(self.c)
        #self.sc.set_offsets(np.c_[frames[0], frames[1]])
        self.plt.pause(0.00000000005)
        #self.fig.canvas.draw_idle()






    def __call__(self,xdata,ydata,newplot=None,color='w',marker=None):
        self.frmdata = [xdata, ydata]
        self.animate_scatter(self.frmdata,color,marker)