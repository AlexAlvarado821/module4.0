"""
Author: Alex Alvarado
Description:
Program: compound_expressions.py
Date:9-19-20
"""


def testMaxandMin(y,x):
    MAX = 10
    MIN = 0

    #y and x are already defined in the function

    if (y > MAX):
        print("Y is larger than the max")
    elif (y < MIN):
        print("Y is smaller than the min")
    else:
        print("Y is either equal to or inbetween the max and min")

    if ( MIN < x < MAX):
        print("X is  in between but not equal to the max or min")
    elif (MIN <= x < MAX):
        print("X is within min but not equal to the max")
    elif(MIN < x <= MAX):
        print("X is above min and within the max")
    else:
        print("X is not equal to the max or min and is not between both values")

if __name__ == '__main__':
    testMaxandMin(3,4)

