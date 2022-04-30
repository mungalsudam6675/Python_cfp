'''
    @Author: SudamMUngal
    @Date: 28-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 28-04-2022 12:01:00
    @Title : Quadratic
'''
import math
import sys

if __name__ == '__main__':
    
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    root1 = float(0)
    root2 = float(0)

    decrement = float((b * b) - 4 * a * c)
    print(decrement)

    if decrement < 0:
        print("Roots Are Imaginary")

    elif (decrement == 0):
        root1 = (-b / 2 * a)
        root2 = (-b / 2 * a)
        print("Root 01 Is: ", root1)
        print("Root 02 Is: ", root2)

    elif decrement > 0:
        root1 = (-b + math.sqrt(decrement / (2 * a)))
        root1 = (-b - math.sqrt(decrement / (2 * a)))
        print("Root 01 Is: ", root1)
        print("Root 02 Is: ", root2)