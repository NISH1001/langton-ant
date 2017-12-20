#!/usr/bin/env python3

from ant import directions, rotate_clockwise, rotate_counterclock
import matplotlib.pyplot as plt
from matplotlib import animation

import random

class MultiLangtonAnt:
    BLACK = 0
    WHITE = 1

    def __init__(self, num_ant=2, grid_size=25):
        self.num_ant = num_ant
        self.grid_size = grid_size
        self.grid = [ [ MultiLangtonAnt.WHITE for j in range(self.grid_size) ] for i in range(self.grid_size)  ]
        self._spawn()

    def _spawn(self):
        self.positions = []
        self.directions = []
        border_gap = int(self.grid_size/3)
        for i in range(self.num_ant):
            r = random.randrange(border_gap, self.grid_size-border_gap)
            c = random.randrange(border_gap, self.grid_size-border_gap)
            self.positions.append([r, c])
            self.directions.append(random.choice(directions))
        print(self.positions, self.directions)

    def _step_single_ant(self, i):
        r, c = self.positions[i][0], self.positions[i][1]
        if self.grid[r][c] == MultiLangtonAnt.WHITE:
            self.directions[i] = rotate_counterclock(self.directions[i])
            self.grid[r][c] = MultiLangtonAnt.BLACK
        else:
            self.directions[i] = rotate_clockwise(self.directions[i])
            self.grid[r][c] = MultiLangtonAnt.WHITE

        self.positions[i][0] -= self.directions[i][1]
        self.positions[i][1] += self.directions[i][0]

    def _step(self):
        for i in range(self.num_ant):
            self._step_single_ant(i)

    def run(self, epoch=1000):
        for i in range(self.num_ant):
            self._step()

def main():
    ants = MultiLangtonAnt(3, 200)
    ants.run()

if __name__ == "__main__":
    main()

