'''
    @Author: SudamMungal
    @Date: 28-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 28-04-2022 12:01:00
    @Title :prints the Euclidean distance from the point (x, y) to the origin (0, 0).
'''
from ast import arg
import math
import sys

if __name__ == '__main__':
    x1 = 0
    y1 = 0

    x2 = int(sys.argv[1])
    y2 = int(sys.argv[2])


    distance = math.sqrt((x2*x2) + (y2*y2))
    print(distance)