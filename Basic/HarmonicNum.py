'''
    @Author: SudamMUngal
    @Date: 27-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 27-04-2022 12:01:00
    @Title : Harmonic Number...
'''
def nThHaromic (nthNum):
    """
        Description:
            Prints the nth Harmonic Number
        Parameter:
             passing nth number
        Return:
            Returning nth harmonic numebr 
    """
    harmonic = 0
    for i in range(2,nthNum+1):
        harmonic += 1 / i 

    return harmonic
    
if __name__ == '__main__':
    num = int(input("Enter Number To Calculate Nth harmonic Number!: \n"))
    print(nThHaromic(num))