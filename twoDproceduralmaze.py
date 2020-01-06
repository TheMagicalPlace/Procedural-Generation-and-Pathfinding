# Random Maze Generator using Depth-first Search
# http://en.wikipedia.org/wiki/Maze_generation_algorithm
# FB - 20121214
# Credit https://code.activestate.com/recipes/578356-random-maze-generator/



import random,copy


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
                    self.plotobj(xy[0],xy[1],False,color='w',marker='s')


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