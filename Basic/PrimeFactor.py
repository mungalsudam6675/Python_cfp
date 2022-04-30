'''
    @Author: SudamMungal
    @Date: 27-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 27-04-2022 12:01:00
    @Title :Computes the prime factorization of N using brute force.
'''
import math

def factor (n):
    """
        Description:
            Prints the factors of numeber
        Parameter:
             passing number for prime factorisation
        Return:
            Returning nothing but printing factors
    """
    primeFactor = []
    divisor = 2

    while divisor <= n:
        if n%divisor == 0:
            primeFactor.append(divisor)
            n = n/divisor
        else:
            divisor+=1
    return primeFactor

if __name__ == '__main__':
  
    num = int(input("Enter Number To Factors Of Number!: \n"))
    print("Factors Of ", num ," Is: ", factor(num))