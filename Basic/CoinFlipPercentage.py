'''
   @Author: SudamMungal
    @Date: 27-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 27-04-2022 12:01:00
    @Title : Flip Coin and print percentage of Heads and Tails
'''
import random
from pip import main

def flipPercentage(head,tail):
    """
        Description:
            calculatinig percenatge of coin flip and printing answer
        Parameter:
            passing head and tail which is calculated
        Return:
            Returning nothing but printing messages
    """
    totalToss = head+tail

    headPercentage = 100 * head / totalToss

    print ("Percentage Of Head is", headPercentage)

    print ("Percentage Of Tail is", abs(headPercentage-100))

def coinFlipCalculation(totalFlip):
    """
        Description:
            getting total flip from parameter and calling function
        Parameter:
            passing total flip by user.
        Return:
            Returning nothing but calling another function
    """
    head = 0
    tail = 0

    for i in range (totalFlip):
        flipCheck = random.randint(0,1)

        if flipCheck == 0:
            head+=1
        else:
            tail+=1
    
    print("Total Head Is ",head)
    print("Total Tail Is ",tail)
    flipPercentage(head,tail)


if __name__ == '__main__':
    
    numOfFlip = int(input("Enter How Many Time Wanna Flip! \n"))
    coinFlipCalculation(numOfFlip)