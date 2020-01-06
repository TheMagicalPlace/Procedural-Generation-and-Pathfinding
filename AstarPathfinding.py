





# from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
import matplotlib.pyplot as plt
import numpy as np
import random,copy,time

from AnimatedPlotMods import liveplot


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position # x-y position on the grid


        # values for heuristic function
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class Pathfinder:

    def __init__(self,maze,start,end,plotobj=None):
        self.plotobj = plotobj # initilize the live plot
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
        open_list = [] # unexplored/possible next node(s) to traverse
        closed_list =[] # explored or non-viable nodes
        open_list.append(self.snode) # initial node

        while len(open_list) > 0:

            current_node = open_list[0] # the next explored node is taken from the top of the list
            current_index = 0

            # checking if there is a better node to look at
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # updates the live plot
            if self.plotobj is not None:
                if closed_list:
                    xy = list(zip(*[n.position for n in closed_list]))
                    if xy:
                        self.plotobj(xy[0],xy[1],False,color='y',marker='x')

                else:
                    # setting initial node values
                    for x in range(0,len(self.maze)):
                        for y in range(0,len(self.maze[x])):
                            if self.maze[x][y]:self.maze[x][y]=0
                            else: self.maze[x][y]=1


            # moving the current node to the closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # checking if the target node has been found
            if current_node == self.enode:
                path = []
                current = current_node

                #self.plotobj.show_solution([], [], color='b', marker='*')
                # going back through parents to findpath
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                    p2 = list(zip(*path))

                    self.plotobj.show_solution(p2[0], p2[1], color='aqua', marker='*')
                return path[::-1]  # Return reversed path

            # only cardinal movments allowed here, i.e. no up, down, left, right
            possible_moves = [(0, -1), (0, 1), (-1, 0), (1, 0)] #(-1, -1), (-1, 1), (1, -1), (1, 1)]

            children = []

            # checking possible child nodes
            for move in possible_moves:
                node_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])

                # the position has to be in the grid, otherwise look at next possible move
                if node_position[0] > (len(self.maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(self.maze[len(self.maze) - 1]) - 1) or node_position[1] < 0:
                    continue

                # can't move onto walls
                if self.maze[node_position[0]][node_position[1]] != 0:
                    continue

                # create a new node and assign it as a child of the parent node
                new_node = Node(current_node,node_position)
                children.append(new_node)

            # looking at child nodes
            for child in children:

                # Child is on the closed list, skip
                for closed_child in closed_list:
                    if child.position == closed_child.position:
                        continue
                # assigning a value to the node
                else:
                    child.g = current_node.g+1 # distance from origin in moves (i.e. no. of nodes between origin and node)


                    # heuristic value, weighed slightly over distance from parent to help avoid the search getting 'stuck'
                    # in cases where the next best node is the parent node and the child node is the best node.
                    child.h = self.value_heuristic(child,self.enode)*1.001 # heuristic value
                    child.f = child.g+child.h

                # in cases where the two 'best' nodes are are the current child node and its parent
                # (i.e. a dead end in the maze close to the exit), the algorithm is likely stalling at a dead end,
                # so in order to allow it to continue the child node is not added to the open list.
                if current_node.parent is not None and child == current_node.parent:
                    continue
                for open_node in open_list:
                    # don't add nodes that are already on the open list
                    if child == open_node or child.g > open_node.g:
                        continue
                open_list.append(child)



    def value_heuristic(self,node1,node2):
        # manhatten distance
        value = abs(node1.position[0]-node2.position[0])+abs(node1.position[1]-node2.position[1])
        return value




