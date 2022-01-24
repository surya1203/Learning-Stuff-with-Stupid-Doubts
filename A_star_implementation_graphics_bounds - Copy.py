from collections import deque
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

grid_map = np.array([[0,0,0,1,0,0,1,1,1,0,1,0,1,0],
                     [1,1,1,0,1,0,1,0,1,0,1,1,1,0],
                     [1,1,1,0,1,1,0,1,1,0,1,0,1,0],
                     [1,0,0,1,0,1,0,1,1,0,0,1,1,0],
                     [0,0,0,0,1,1,1,1,0,1,1,1,1,0],
                     [0,1,1,0,0,1,0,0,0,1,0,0,0,0],
                     [1,1,0,1,1,0,0,0,1,1,0,0,0,0],
                     [1,1,0,1,0,1,0,1,0,0,1,1,0,1],
                     [1,1,1,0,1,0,1,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,1,0,1,0,1,1,0,0],
                     [0,0,0,0,0,0,0,0,1,0,1,0,0,1],
                     [1,0,0,0,0,0,0,0,1,0,1,0,1,1],
                     [1,1,0,0,0,1,1,1,1,0,0,0,1,1],
                     [1,1,0,1,0,1,0,0,1,1,0,1,0,0],
                     [0,0,0,1,1,1,0,0,1,1,0,0,0,0],
                     [0,0,1,0,0,0,0,0,0,1,1,0,0,0],
                     [1,0,1,1,0,1,0,0,0,1,1,0,0,0],
                     [0,0,1,0,0,1,0,1,0,1,1,0,1,0],
                     [1,0,0,0,0,1,1,1,0,1,0,0,0,0],
                     [0,0,0,1,0,0,1,0,0,1,0,1,0,1],
                     [0,0,0,1,0,0,0,1,0,0,0,1,1,0],
                     [0,0,0,1,1,1,1,1,1,1,1,0,1,1],
                     [1,1,1,1,1,1,0,0,0,1,0,1,0,0],
                     [0,0,1,1,0,0,0,0,0,0,1,0,1,1],
                     [1,1,1,1,0,1,0,1,0,0,1,1,1,1],
                     [1,1,1,1,0,1,0,1,1,0,0,1,0,1],
                     [0,1,0,0,0,0,1,0,0,0,0,0,1,0],
                     [0,1,0,0,1,0,1,0,0,0,1,0,1,0],
                     [1,1,0,1,1,1,1,1,0,0,1,0,1,0]])

bounds = [grid_map.shape[0]-1, grid_map.shape[1]-1]
# print(bounds)


class A_Star:
    # @staticmethod
    # def draw_graph(point, obstacles: list, marking="|*|"):
    #     height = 10
    #     width = 10
    #     for y_point in range(0, width):
    #         for x_point in range(0, height):
    #             if (x_point, y_point) in obstacles:
    #                 print('|X|', end='')
    #             elif (x_point, y_point) in point:
    #                 print(marking, end='')
    #             else:
    #                 print('| |', end='')
    #         print()

    def find_obstacles(self, grid_map: np.array):
        obstacles_in_arrays = np.where(grid_map == 1)
        print(obstacles_in_arrays)
        list_of_obstacles = list(zip(obstacles_in_arrays[0], obstacles_in_arrays[1]))
        obstacles = [obstacle for obstacle in list_of_obstacles]
        # print(obstacles)
        return obstacles

    def distance_to_neighbour(self, previous_cell, current_cell) -> float:
        x1, y1 = previous_cell
        x2, y2 = current_cell
        # distance = abs(x2 - x1) + abs(y2 - y1)
        modifier = 0
        adjusted_cost = 1.000
        # if (x1 + y1) % 2 == 0 and x2 != x1 and y2 != y1:
        #     modifier = 2
        # if (x1 + y1) % 2 == 1 and y2 != y1 and x2 != x1:
        #     modifier = 2
        # if (x1 + y1) % 2 == 0 and x2 != x1:
        #     modifier = 1
        # if (x1 + y1) % 2 == 1 and y2 != y1:
        #     modifier = 1
        if (x1+y1) % 2 == (x2+y2) % 2:
            modifier = 1
        adjusted_cost = 1 + 0.1 * modifier
        return adjusted_cost

    def get_neighbours(self, cell, obstacles: list):
        X, Y = bounds
        x, y = cell
        neighbour_list = []
        neighbours = [(x+1, y), (x, y-1), (x-1, y), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
        if 0 <= x <= X and 0 <= y <= Y:
            neighbour_list = [neighbour for neighbour in neighbours if neighbour not in obstacles]
        # print(X,Y)
        return neighbour_list

    def get_closest_cell(self, open_set, f_score):
        smallest_distance = float('inf')
        closest_cell = None
        for cell in open_set:
            if f_score[cell] < smallest_distance:
                smallest_distance = f_score[cell]
                closest_cell = cell
        return closest_cell

    def heuristic_function(self, point1, point2) -> float:
        x1, y1 = point1
        x2, y2 = point2
        dx=(x1-x2)
        dy=(y1-y2)
        d=((dx**2)+(dy**2))
        return np.sqrt(d)

    def path(self, previous_cell, finish):
        path = deque()
        cell = finish
        path.appendleft(cell)
        while cell in previous_cell:
            cell = previous_cell[cell]
            path.appendleft(cell)
        print(path)
        return path

    def A_star(self, start, finish, obstacles: list):
        open_set = set([start])
        closed_set = set()
        previous_cell = {}
        f_score = {}
        g_score = {}    # movement cost from start to current point
        g_score[start] = g_score.setdefault(start, 0)
        h_score = self.heuristic_function(start, finish)    # movement cost from current cell to finish
        f_score[start] = f_score.setdefault(start, 0)
        f_score[start] = g_score[start] + h_score
        while open_set:
            current_cell = self.get_closest_cell(open_set, f_score)
            if current_cell == finish:
                return self.path(previous_cell, finish)
            open_set.remove(current_cell)
            neighbours = None
            neighbours = self.get_neighbours(current_cell, obstacles)
            print()
            try:
                print(current_cell,f_score[(8, 8)])
            except KeyError:
                pass
            print(f_score[current_cell])
            print(closed_set)
            print(open_set)
            for neighbour in neighbours:
                current_g_score = g_score[current_cell] + self.distance_to_neighbour(current_cell, neighbour)
                h_score = self.heuristic_function(neighbour, finish)
                # lol=g_score[neighbour]
                # try:
                #     print(neighbour,current_g_score,h_score,g_score[neighbour])
                # except KeyError:
                #     pass
                if neighbour in closed_set and current_g_score >= g_score[neighbour]:
                    continue
                if neighbour not in closed_set or current_g_score < g_score[neighbour]:
                    try:
                        print(neighbour,current_g_score,h_score,g_score[neighbour])
                    except KeyError:
                        pass
                    previous_cell[neighbour] = current_cell
                    g_score[neighbour] = current_g_score
                    f_score[neighbour] = g_score[neighbour] + h_score
                    try:
                        print(neighbour,current_g_score,h_score,g_score[neighbour])
                    except KeyError:
                        pass
                    if neighbour not in open_set:
                        open_set.add(neighbour)
            closed_set.add(current_cell)


implement = A_Star()
start = (0, 0)
finish = (22, 13)
obstacles = implement.find_obstacles(grid_map)
path = False
try:
    path = list(implement.A_star(start, finish, obstacles))
except TypeError:
    print("No path found.")

if path:
    color_map = colors.ListedColormap(['white', 'black'])
    plt.imshow(grid_map, cmap=color_map)
    plt.plot(np.asarray(path)[:, 1], np.asarray(path)[:, 0])

    plt.show()


