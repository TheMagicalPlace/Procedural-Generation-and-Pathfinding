from twoDproceduralmaze import maze_generator
from AstarPathfinding import *






if __name__ == '__main__':
    x, y = 51, 51 # grid size
    plot_obj = liveplot(x, y) # init live plot

    mgen = maze_generator(x, y, plot_obj) # create a new maze
    maze, end, start = mgen()

    p = Pathfinder(maze, (start[1], start[0]), (end[0], end[1]), plot_obj)
    p()
    plt.waitforbuttonpress()