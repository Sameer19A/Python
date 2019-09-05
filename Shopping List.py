#Task 6
#Compulsory Task 2


Prod1 = input("Please enter the name of product 1: ")
Price1 = float(input("Please enter the price of product 1 (including decimals): "))

Prod2 = input("\nPlease enter the name of product 2: ")
Price2 = float(input("Please enter the price of product 2 (including decimals): "))

Prod3 = input("\nPlease enter the name of product 3: ")
Price3 = float(input("Please enter the price of product 3 (including decimals): "))


Total = Price1 + Price2 + Price3
Avg = Total/3

print("\nThe Total of", Prod1,Prod2,Prod3,"is R",Total,"and the average price of the items are R",Avg)
