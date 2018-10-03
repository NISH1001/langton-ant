#!/usr/bin/env python3

from multiant import MultiLangtonAnt
import matplotlib.pyplot as plt
from matplotlib import animation

import sys

class Animator:
    def __init__(self, ant):
        self.ant = ant

    def _animate(self, i):
        self.ant._step()
        self.img.set_data(self.ant.grid)
        return [self.img]

    def animate(self, num_frames=1000):
        fig = plt.figure()
        self.img = plt.imshow(self.ant.grid, interpolation='none', vmin=0, vmax=1)
        anim = animation.FuncAnimation(fig, self._animate,
                               frames=num_frames, interval=0, blit=True,
                               repeat=False)
        plt.show()


def main():
    n = sys.argv[1:]
    if not n:
        n = 2
        print("Using default ant number :: {}".format(n))
    else:
        n = int(n[0])
        print("Using ant number :: {}".format(n))
    ants = MultiLangtonAnt(n, 100 * n)
    animator = Animator(ants)
    animator.animate(50000)

if __name__ == "__main__":
    main()

