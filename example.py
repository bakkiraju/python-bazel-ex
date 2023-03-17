# Example that uses absl, scipy, numpy packages 
from absl import app
from absl import flags
from absl import logging

import matplotlib.pyplot as plt
import numpy as np

from math import cos             # cosine
from scipy.optimize import root
from scipy.spatial import ConvexHull

import sys

def calc_convex_hull(points):
    hull = ConvexHull(points)
    hull_points = hull.simplices
    return hull_points

def non_linear_equation(x):
    return x + cos(x)

def plot_convex_hull(points,hull_points):
    plt.scatter(points[:,0], points[:,1])
    for simplex in hull_points:
        plt.plot(points[simplex,0], points[simplex,1], 'k-')
    plt.show()

FLAGS = flags.FLAGS

flags.DEFINE_string('echo', None, 'Text to echo.')

def main(argv):
    del argv  # Unused.

    print('Running under Python {0[0]}.{0[1]}.{0[2]}'.format(sys.version_info),
        file=sys.stderr)
    logging.info('echo is %s.', FLAGS.echo)

    solution = root(non_linear_equation, 0)
    logging.info('x+cos(x) root: %s',str(solution.x))
 
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    logging.info('original array: \n%s',str(arr))
    newarr = arr.reshape(4, 3)
    logging.info('reshaped array: \n%s',str(newarr))
    
    points = np.array([[0, 2],[1, 3], [0, 3],[1, 1],[3, 0], [2, 3],[4, 1],[3, 5],[0, 1],[2, 0]])
    logging.info("Given points: \n%s", str(points))
    hull_points = calc_convex_hull(points)
    logging.info("convex hull of the above points: \n%s", str(hull_points))
    plot_convex_hull(points,hull_points)
    
if __name__ == '__main__':
   app.run(main)


