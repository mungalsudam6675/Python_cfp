'''
   @Author: SudamMUngal
    @Date: 27-04-2022 11:26:00
    @Last Modified by: MungalSudam
    @Last Modified time: 27-04-2022 12:01:00
    @Title : Flip Coin and print percentage of Heads and Tails
'''
def greet (name):
    """
        Description:
            Prints the Greeting Message
        Parameter:
            passing name varible with user name for sending name with greeting message
        Return:
            Returning nothing but printing messages
    """

    print("Hello", name)
    print("How Are You!")

if __name__ == '__main__':
    userName = input("Enter User userName: \n")
    while True:
        if len(userName) < 3:
            userName = input("Enter Valid User userName Needed Minimum 3 Charecter: \n")
        else:
            break

    greet(userName)