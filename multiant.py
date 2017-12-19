#!/usr/bin/env python3

from ant import LangtonAnt
import matplotlib.pyplot as plt
from matplotlib import animation

import random

class MultiLangtonAnt:
    """
        Wrapper over single Lanton's Ant
    """
    def __init__(self, num_ant=2, grid_size=10):
        self.num_ant = num_ant
        self.grid_size = grid_size
        # the global grid
        self.grid = [ [ LangtonAnt.WHITE for j in range(grid_size) ] for i in range(grid_size)  ]
        self._spawn()

    def _spawn(self):
        """
            Spwan 'n' number of ants in random place
        """
        self.ants = []
        border_gap = int(self.grid_size/3)
        for i in range(self.num_ant):
            ant = LangtonAnt(self.grid_size)
            ant.ant_r = random.randrange(border_gap, self.grid_size-border_gap)
            ant.ant_c = random.randrange(border_gap, self.grid_size-border_gap)
            self.ants.append(ant)

    def _step(self):
        for i, ant in enumerate(self.ants):
            self.ants[i].step()
            # now update the global grid state using the individual ant's grid
            for row in range(self.grid_size):
                for col in range(self.grid_size):
                    self.grid[row][col] |= self.ants[i].grid[row][col]
            self.ants[i].grid = self.grid

    def run(self, epoch=1000):
        for i in range(epoch):
            self._step()

def main():
    ants = MultiLangtonAnt(3, 200)
    ants.run(1000)

if __name__ == "__main__":
    main()

