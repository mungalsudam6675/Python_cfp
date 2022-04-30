'''
    @Author: SudamMUngal
    @Date: 29-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 29-04-2022 12:01:00
    @Title : A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
'''
import array

def addAndPrint2DArray (rows,cols):
    """
        Description:
            adding values in 2D Array
        Parameter:
            rows and colums
        Return:
            Returning nothing but printing and adding array
    """

    arr = []  
    for i in range(rows):  
        row = []  
        for j in range(cols):
            num = int(input("Enter the matrix"))  
            row.append(num)  
        arr.append(row)

    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

addAndPrint2DArray(3,2)