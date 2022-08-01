# lets calculate the expense of car service 
"""
1.ask user to enter their cost in car mantainec and assign it to tthe variable with the name respectively
2.change all the input to floar value .
3.declare a variable with a name totacost.
4.add all the cost and assign it to the variable totalcost.
5. print total cost.
"""

oilChange=float(input("how much you spend on oil change? "))
tyreRotation=float(input("how much they charge for tyre rotation? "))
alignment=float(input("how much is for alignment? "))
airPressuer=float(input("airpressure check cost "))
inspectingBattery=float(input("battery inspection cost? "))
gas=float(input("how much you spend on gas? "))
carwash=float(input("cost for carwash "))
filterChange=float(input("how much does filter cost? "))
totalCost=oilChange+tyreRotation+alignment+airPressuer+inspectingBattery+gas+carwash+filterChange 
print("total cost for your car service is  ",totalCost