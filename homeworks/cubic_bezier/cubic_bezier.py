import numpy as np
import sys
from scipy.special import binom

import matplotlib.pyplot as plt

from matplotlib.lines import Line2D

class BezierBuilder(object):
    def __init__(self, ax_main, line=None):
        self.line = line
        if line is not None:
            self.xp = list(line.get_xdata())
            self.yp = list(line.get_ydata())
        else:
            self.xp = []
            self.yp = []
        self.canvas = ax_main.figure.canvas
        self.ax_main = ax_main

        self.cid = self.canvas.mpl_connect('button_press_event', self)
        line_bezier = Line2D([], [], c='red')
        self.bezier_curve = self.ax_main.add_line(line_bezier)

    def __call__(self, event):
        if event.inaxes != self.ax_main:
            return

        self.xp.append(event.xdata)
        self.yp.append(event.ydata)
        if self.line is not None:
            self.line.set_data(self.xp, self.yp)

        self.bezier_curve.set_data(*self._build_bezier())
        self._update_bezier()

    def _build_bezier(self):
        x, y = Bezier(list(zip(self.xp, self.yp))).T
        return x, y

    def _update_bezier(self):
        self.canvas.draw()

def Bernstein(n, k):
    coeff = binom(n, k)
    def _bpoly(x):
        return coeff * x**k * (1 - x)**(n - k)
    return _bpoly

def Bezier(points, num=200):
    N = len(points)
    t = np.linspace(0, 1, num=num)
    curve = np.zeros((num, 2))
    for ii in range(N):
        curve += np.outer(Bernstein(N - 1, ii)(t), points[ii])
    return curve

if __name__ == '__main__':
    fig, ax1 = plt.subplots(1, 1, figsize=(12, 5))
    
    hidden = False
    
    if len(sys.argv) > 1:
      hidden = sys.argv[1] == 'hidden'
    
    line = None
    if not hidden:
        line = Line2D([], [], ls='--', c='#666666',
                marker='x', mew=2, mec='#204a87')
        ax1.add_line(line)

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_title("Bezier curve")

    bezier_builder = BezierBuilder(ax1, line)

    plt.show()