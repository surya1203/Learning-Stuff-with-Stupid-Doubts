import math
from collections import deque

#
# finish = [7, 8]
# start = [1, 3]
# draw_graph(start)
# draw_graph(finish)


class AStar:
    @staticmethod
    def draw_graph(point, obstacles: list, marking="|*|"):
        height = 10
        width = 10
        for y_point in range(0, width):
            for x_point in range(0, height):
                if (x_point, y_point) in obstacles:
                    print('|X|', end='')
                elif (x_point, y_point) in point:
                    print(marking, end='')
                else:
                    print('| |', end='')
            print()

    def distance_to_neighbour(self, previous_cell, current_cell) -> float:
        x1, y1 = previous_cell
        x2, y2 = current_cell
        # distance = abs(x2 - x1) + abs(y2 - y1)
        modifier = 0
        if (x1 + y1) % 2 == 0 and x2 != x1 and y2 != y1:
            modifier = 1.0001
        if (x1 + y1) % 2 == 1 and y2 != y1 and x2 != x1:
            modifier = 1.0001
        if (x1 + y1) % 2 == 0 and x2 != x1:
            modifier = 1
        if (x1 + y1) % 2 == 1 and y2 != y1:
            modifier = 1
        adjusted_cost = 1 + 0.001 * modifier
        return adjusted_cost

    def get_neighbours(self, cell, obstacles):
        neighbour_list = []
        x, y = cell
        neighbours = [(x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
        neighbour_list = [neighbour for neighbour in neighbours if neighbour not in obstacles]
        print(neighbour_list)
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
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def path(self, previous_cell, finish):
        path = deque()
        cell = finish
        path.appendleft(cell)
        while cell in previous_cell:
            cell = previous_cell[cell]
            path.appendleft(cell)
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
        while open_set is not None:
            current_cell = self.get_closest_cell(open_set, f_score)
            if current_cell == finish:
                return self.path(previous_cell, finish)
                # pass
            open_set.remove(current_cell)
            neighbours = None
            neighbours = self.get_neighbours(current_cell, obstacles)
            for neighbour in neighbours:
                current_g_score = g_score[current_cell] + self.distance_to_neighbour(current_cell, neighbour)
                h_score = self.heuristic_function(neighbour, finish)
                if neighbour in closed_set and current_g_score >= g_score[neighbour]:
                    continue
                if neighbour not in closed_set or current_g_score < g_score[neighbour]:
                    previous_cell[neighbour] = current_cell
                    g_score[neighbour] = current_g_score
                    f_score[neighbour] = g_score[neighbour] + h_score
                    if neighbour not in open_set:
                        open_set.add(neighbour)
            closed_set.add(current_cell)


implement = AStar()
start = (1, 3)
finish = (7, 6)
obstacles = [(2, 3), (3, 3), (3, 4), (4, 3), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9)]
starting_list = [start, finish]
print(f'Starting co-ordinate: {start}\nFinishing co-ordinate: {finish}')
implement.draw_graph(starting_list, obstacles, marking='@')
plot = list(implement.A_star((1, 3), (7, 6), obstacles))
print()
print('===============================')
print()
implement.draw_graph(plot, obstacles)

