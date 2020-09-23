"""
Author: Alex Alvarado
Program: basic-ifelif
Description: asks the user for their membership and outputs the included items in their subscription.
Date: 9-19-20
"""


def chooseMembership():
    selection = input("Please enter the membership you wish to purchase from the following list: \n Platinum \n Gold \n Silver \n Bronze \n Free Trial \n : -->")
    print ("You choose : " + selection)
    selection.lower()
    if (selection == 'platinum'):
        print("The platinum membership costs 60 dollars and includes the subscritption box four free suprize gifts alongside two t-shirts")
    elif (selection == 'gold'):
        print("The gold membership cost 50 dollars and includes the subsciption box and two free suprize gifts alongside a t-shirt")
    elif (selection == 'silver'):
        print("The silver membership costs 40 dollars and includes the subcription box and one free suprize gift alongside an additional tool")
    elif (selection == 'bronze'):
        print("The bronze membership costs 30 dollars and includes the subscription box and an additional tool")
    elif (selection == 'free trail'):
        print("The free trial includes a reduced size subscription box for 1 month")



if __name__ == '__main__':
    chooseMembership()

