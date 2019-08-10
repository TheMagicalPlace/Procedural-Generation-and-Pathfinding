


from matplotlib import pyplot as plt
import matplotlib.animation
import numpy as np
import copy


class liveplot:
    ''' animated plot generation for 2-dimensional plots'''
    def __init__(self,x_axis,y_axis,x=[],y=[]):
        self.plt = plt
        self.plt.ion()
        self.fig, self.ax = plt.subplots()
        x, y  = [1],[1]
        self.sc = self.ax.scatter(x, y,marker='D',c='black') # TODO give functionality to more than just scatter plots
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

    def animate_scatter(self,frames,color='g'):

        self.sc.set_offsets(np.c_[frames[0], frames[1]])
        self.fig.canvas.draw_idle()
        self.plt.pause(0.005)




    def __call__(self,xdata,ydata,newplot=None,color='w',marker=None):
        self.frmdata = [xdata, ydata]
        if newplot:
            self.animate_scatter(self.frmdata,'g')
            self.sc = self.ax.scatter(self.frmdata[0], self.frmdata[1], marker=marker, c=color)
        else:
            self.animate_scatter(self.frmdata,'y')
            #self.sc = self.ax.scatter(self.frmdata[0], self.frmdata[1], marker='X', c=color)
