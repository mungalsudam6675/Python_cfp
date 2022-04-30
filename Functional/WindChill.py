'''
    @Author: SudamMUngal
    @Date: 27-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 27-04-2022 12:01:00
    @Title :  prints the wind chill.
'''
import sys
import math

if __name__ == '__main__':
    t = float(sys.argv[1])
    v = float(sys.argv[2])

    if t < 50 and v < 120 and v > 3:
        windChill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v,0.16)
        print("Wind Chill Is: " + math.floor(windChill))
    else:
        print("Values Are Not Valid ")