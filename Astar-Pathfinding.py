





# from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
import matplotlib.pyplot as plt
import numpy as np
import random,copy,time

from AnimatedPlotMods import liveplot


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class Pathfinder:
    def __init__(self,maze,start,end,plotobj=None):
        self.plotobj = plotobj
        self.maze = maze
        self.start = start
        self.end = end
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0
        self.snode = start_node
        self.enode = end_node

    def __call__(self, *args, **kwargs):
        return self.pathfinder()

    def pathfinder(self):
        open_list = []
        closed_list =[]
        open_list.append(self.snode)
        pflag = True
        while len(open_list) > 0:

            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f: #########################
                    current_node = item
                    current_index = index

            if self.plotobj is not None:
                if closed_list:
                    xy = list(zip(*[n.position for n in closed_list]))
                    if xy:
                        self.plotobj(xy[0],xy[1],False,color='y',marker='x')

                else:
                    xy,yz = maze_generator.maze_view(None,copy.deepcopy(self.maze))
                    self.plotobj(xy[0], xy[1], True, color='yellow',marker='x')
                    pflag = False
                    for x in range(0,len(self.maze)):
                        for y in range(0,len(self.maze[x])):
                            if self.maze[x][y]:self.maze[x][y]=0
                            else: self.maze[x][y]=1

            open_list.pop(current_index)
            closed_list.append(current_node)
            if current_node == self.enode:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                    p2 = list(zip(*path))
                    if len(path) <=1:
                        self.plotobj(xy[0], xy[1], True, color='aqua',marker='*')
                    else:
                        self.plotobj(p2[0],p2[1],False,color='b')
                return path[::-1]  # Return reversed path


            possible_moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]#(-1, -1), (-1, 1), (1, -1), (1, 1)] #only includes directly adjacent, no diag

            children = []
            for move in possible_moves:
                node_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])

                if node_position[0] > (len(self.maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(self.maze[len(self.maze) - 1]) - 1) or node_position[1] < 0:
                    continue

                if self.maze[node_position[0]][node_position[1]] != 0:
                    continue
                new_node = Node(current_node,node_position)
                children.append(new_node)

            for child in children:

            # Child is on the closed list
                for closed_child in closed_list:
                    if child.position == closed_child.position:
                        continue
                else:
                    child.g = current_node.g+1
                    child.h = self.value_heuristic(child,self.enode)*1.001
                    child.f = child.g+child.h

                if current_node.parent is not None and child == current_node.parent:
                    continue
                for open_node in open_list:
                    if child == open_node or child.g > open_node.g:
                        continue
                open_list.append(child)



    def value_heuristic(self,node1,node2):
        value = abs(node1.position[0]-node2.position[0])+abs(node1.position[1]-node2.position[1])
        return value

class maze_generator:


    def __init__(self,xlen,ylen,plot_obj=None):
        if plot_obj is not None:
            self.plotobj = plot_obj
        else:
            self.plotobj = None
        self.mx = xlen
        self.my = ylen  # width and height of the maze
        self.maze = [[0 for x in range(self.mx)] for y in range(self.my)]
        self.dx = [0, 1, 0, -1];
        self.dy = [-1, 0, 1, 0]  # 4 directions to move in the maze
        self.stack = [(len(self.maze)-2, len(self.maze[1])-1)]
        self.start = copy.copy(self.stack[0])
        color = [(0, 0, 0), (255, 255, 255)]  # RGB colors of the maze

    def __call__(self, *args, **kwargs):
        self.maze_generator()
        return self.maze,self.end,self.start

    def maze_view(self,maze):
        xy = []
        yz = []
        maze = copy.deepcopy(maze)
        for i in range(0,len(maze)):
            for j in range(0,len(maze[i])):
                if maze[i][j] or maze[i][j] ==2:
                    maze[i][j] = '  '
                    xy.append((i, j))
                else:
                    maze[i][j] = '[]'
                    yz .append((i,j))

            #print("".join(maze[i]))
        return list(zip(*xy)),list(zip(*yz))

    def maze_generator(self):
        flag = True
        fla2g = False
        while len(self.stack) > 0:
            if self.plotobj is not None:
                xy,yz = self.maze_view(self.maze)
                if xy:
                    self.plotobj(xy[0],xy[1],False,marker='+')
                else:
                    self.plotobj(yz[0],yz[1],flag,marker='s',color='w')
                    flag = False

            (cx, cy) = self.stack[-1]
            self.maze[cy][cx] = 1
            # find a new cell to add
            nlst = [] # list of available neighbors
            for i in range(4):
                nx = cx + self.dx[i]; ny = cy + self.dy[i]
                if nx >= 1 and nx < self.mx-1 and ny >= 1 and ny < self.my-1:

                    if self.maze[ny][nx] == 0:
                        # of occupied neighbors must be 1
                        ctr = 0
                        for j in range(4):
                            ex = nx + self.dx[j]; ey = ny + self.dy[j]
                            if ex >= 0 and ex < self.mx and ey >= 0 and ey < self.my:
                                if self.maze[ey][ex] == 1 or self.maze[ey][ex]== 2: ctr += 1
                        if ctr == 1: nlst.append(i)

            # if 1 or more neighbors available then randomly select one and move
            if len(nlst) > 0:
                ir = nlst[random.randint(0, len(nlst) - 1)]
                cx += self.dx[ir]; cy += self.dy[ir]
                if cx == self.mx-1 or cy == self.my-1:
                    self.maze[ny][nx] = 2
                self.stack.append((cx, cy))
            else: self.stack.pop()
        f = True
        for x in range(0,len(self.maze)) :
                if not f: break
                for y in range(0,len(self.maze[x])):
                        if self.maze[y][x+1] == 1:
                            self.maze[x][y] = 1
                            self.end = (x,y)
                            f = False
                            break
        xy,yz = self.maze_view(self.maze)
        self.plotobj(xy[0], xy[1], False)
        return xy

aze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

x,y =101,101
plot_obj = liveplot(x,y)
mgen = maze_generator(x,y,plot_obj)
maze,end,start = mgen()
p = Pathfinder(maze,(start[1]//2,start[0]//2),(end[0],end[1]),plot_obj)
print(p())
plt.waitforbuttonpress()

