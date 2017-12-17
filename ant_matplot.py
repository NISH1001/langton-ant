#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import animation
import time

#fig = plt.gcf()
#fig.show()
#fig.canvas.draw()

UP = [0, 1]
DOWN = [0, -1]
LEFT = [-1, 0]
RIGHT = [1, 0]

def rotate_clockwise(vec):
    return [ vec[1], -vec[0] ]

def rotate_counterclock(vec):
    return [ -vec[1], vec[0] ]

class LangtonAnt:
    BLACK = 1
    WHITE = 0
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [ [ LangtonAnt.WHITE for j in range(self.grid_size) ] for i in range(self.grid_size)  ]
        self._initialize_ant(grid_size)

    def _initialize_ant(self, size):
        self.ant_r, self.ant_c = int(self.grid_size/2), int(self.grid_size/2)
        self.direction = UP

    def _animate(self, i):
        self._step()
        self.img.set_data(self.grid)
        return [self.img]

    def run(self, epoch=1000):
        fig = plt.figure()
        self.img = plt.imshow(self.grid, interpolation='none', vmin=0, vmax=1)
        anim = animation.FuncAnimation(fig, self._animate,
                               frames=epoch, interval=0, blit=True,
                               repeat=False)
        plt.show()

    def _step(self):
        r, c = self.ant_r, self.ant_c
        if self.grid[r][c] == LangtonAnt.WHITE:
            self.direction = rotate_counterclock(self.direction)
            self.grid[r][c] = LangtonAnt.BLACK
        else:
            self.direction = rotate_clockwise(self.direction)
            self.grid[r][c] = LangtonAnt.WHITE

        if self.direction == UP:
            r -= 1
        elif self.direction == DOWN:
            r += 1
        elif self.direction == LEFT:
            c -= 1
        else:
            c += 1
        self.ant_r, self.ant_c = r, c

    def __str__(self):
        r, c = self.ant_r, self.ant_c
        curr = self.grid[r][c]
        self.grid[r][c] = '*'
        ret = ""
        for row in self.grid:
            for x in row:
                ret += str(x) + " "
            ret += "\n"
        self.grid[r][c] = curr
        return ret.strip()

def main():
    ant = LangtonAnt(100)
    ant.run(5000)


if __name__ == "__main__":
    main()

