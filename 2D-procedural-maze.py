# Random Maze Generator using Depth-first Search
# http://en.wikipedia.org/wiki/Maze_generation_algorithm
# FB - 20121214
# Credit https://code.activestate.com/recipes/578356-random-maze-generator/



import random
imgx = 500; imgy = 500
mx = 50; my = 50 # width and height of the maze
maze = [[0 for x in range(mx)] for y in range(my)]
dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
color = [(0,0, 0), (255, 255, 255)] # RGB colors of the maze
# start the maze from a random cell
stack = [mx - 1, random.randint(0, my - 1))]

while len(stack) > 0:
    (cx, cy) = stack[-1]
    maze[cy][cx] = 1
    # find a new cell to add
    nlst = [] # list of available neighbors
    for i in range(4):
        nx = cx + dx[i]; ny = cy + dy[i]
        if nx >= 0 and nx < mx and ny >= 0 and ny < my:
            if maze[ny][nx] == 0:
                # of occupied neighbors must be 1
                ctr = 0
                for j in range(4):
                    ex = nx + dx[j]; ey = ny + dy[j]
                    if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                        if maze[ey][ex] == 1: ctr += 1
                if ctr == 1: nlst.append(i)
    # if 1 or more neighbors available then randomly select one and move
    if len(nlst) > 0:
        ir = nlst[random.randint(0, len(nlst) - 1)]
        cx += dx[ir]; cy += dy[ir]
        stack.append((cx, cy))
    else: stack.pop()

#print('[]'*((len(maze)+2)))
#for maze in maze:
#    for i in range(0,len(maze)):
#        if maze[i] == 1:
#            maze[i] = '  '
#        elif maze[i] == 0:
#            maze[i] = '[]'
#    maze.insert(0,'[]')
#    maze.append('[]')

#    print("".join(maze))
#print('[]' * (len(maze)))

import random
imgx = 500; imgy = 500
mx = 10; my = 10; mz = 10 # width and height of the maze
maze = [[[0 for x in range(mx)] for y in range(my)] for z in range(mz)]
dx = [0, 1, 0, -1,0,0]; dy = [-1, 0, 1, 0,0,0]; dz = [0, 0 ,0 ,0,1,-1] # 4 directions to move in the maze
color = [(0,0, 0), (255, 255, 255)] # RGB colors of the maze
# start the maze from a random cell
stack = [(random.randint(0, mx - 1), random.randint(0, my - 1),random.randint(0, mz-1))]

import numpy as np
#modifying to support z
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

while len(stack) > 0:
    (cx, cy, cz) = stack[-1]
    maze[cz][cy][cx] = 1
    # find a new cell to add
    nlst = [] # list of available neighbors
    for i in range(6):
        nx = cx + dx[i]; ny = cy + dy[i]; nz = cz + dz[i]
        if nx >= 0 and nx < mx and ny >= 0 and ny < my and nz >= 0 and nz < mz:
            if maze[nz][ny][nx] == 0:
                # of occupied neighbors must be 1
                ctr = 0
                for j in range(6):
                    ex = nx + dx[j]; ey = ny + dy[j]; ez = nz + dz[j]
                    if ex >= 0 and ex < mx and ey >= 0 and ey < my and ez >= 0 and ez < mz:
                        if maze[ez][ey][ex] == 1: ctr += 1
                if ctr == 1: nlst.append(i)
    # if 1 or more neighbors available then randomly select one and move
    if len(nlst) > 0:
        ir = nlst[random.randint(0, len(nlst) - 1)]
        cx += dx[ir]; cy += dy[ir]; cz += dz[ir]
        stack.append((cx, cy,cz))
    else: stack.pop()
x = []
y = []
z = []
a = []
b = []
c = []
mze = np.ndarray(shape=(10,10,10))
for i in range(0,len(maze)):
    for j in range(0,len(maze[i])):
        for k in range(0,len(maze[i][j])):
            if maze[i][j][k] == 0:
                mze[k,j,i] = 1
#ax.scatter3D(a[1:49],b[1:49],c[1:49])
#ax.scatter3D(mze[:,1,1],mze[1,:,1],mze[1,1,:])
#ax.scatter3D(a,b,c, cmap='Reds')

z,y,x = mze.nonzero()
#a,b,c = mze
#a,b,c = [aa for aa in a if a not in z],[ab for ab in b if b not in y],[ac for ac in c if c not in x]


ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z,c=z)
plt.show()
plt.savefig("demo.png")