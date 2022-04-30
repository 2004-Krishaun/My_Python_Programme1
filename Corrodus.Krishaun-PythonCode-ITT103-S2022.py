#Author: Krishaun Corrodus
#Date Created: April 28, 2022
#Course: ITT103
#Purpose: The purpose of this code is to show my efficience and skills in within a Python Code

Class_1a_rate = 0.06
Class_1b_rate = 0.07
Class_1c_rate = 0.10

Class_2a_rate = 0.04
Class_2b_rate = 0.06

Class_3_rate = 0.045

Salesperson_num= int(input("Input salesperson number"))
while Salesperson_num != 0:
    Salesperson_num= int(input("Please to enter your salesperson number:"))
    Sales_amount=int(input("Please to enter your Sales amount:"))
    Class=int(input("Please to enter your Class number:"))
    if Class == 1:
        if Sales_amount <= 1000:
            print ("Your commission rate is:", Sales_amount * Class_1a_rate)
    if Class == 1:
        if Sales_amount > 1000 and Sales_amount < 2000:
            print("Your comission rate is:",Sales_amount * Class_1b_rate)
    if Class == 1:
        if Sales_amount >= 2000:
            print ("Your comission rate is:", Sales_amount * Class_1c_rate)
    elif Class == 2:
        if Sales_amount < 1000:
            print ("Your comission rate is:", Sales_amount * Class_2a_rate)
    if Class == 2:
        if Sales_amount >= 1000:
            print ("Your comission rate is:", Sales_amount * Class_2b_rate)
    if Class == 3:
        print("Your commision rate is:", Sales_amount * Class_3_rate)
    elif Class > 3:
        print(" An Error have occurred. Please to select a Class from 1-3.")

    i=input("Would you like to continue? Yes or No?")
    if i =="No":
        break

"End"
