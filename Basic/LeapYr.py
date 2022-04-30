'''
    @Author: SudamMungal
    @Date: 27-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 27-04-2022 12:01:00
    @Title : Leap Year
'''


def leapYearCheck(year):
    """
        Description:
            Print the year is a Leap Year or not.
        Parameter:
            passing int variable as year
        Return:
            Returning Nohting but printing statement year is leap or Not
    """

    if (year % 4) == 0:

        if (year % 100) and (year % 400) == 0: #is a century year
                print(year, "Is Leap A Year")
        else:
            print(year, "Is Not A Leap Year")

    else:
            print(year, "Is Not A Leap Year")

if __name__ == '__main__':
    while True:
        checkYear = int(input("Enter a Year You Want To Check Leap Year Or Not ?"))

        if (checkYear > 9999) or (checkYear < 1000):
            checkYear = int(input("Please, Enter Valid Year "))
            leapYearCheck(checkYear)
            break

        else:
            leapYearCheck(checkYear)
            break