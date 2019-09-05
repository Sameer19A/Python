#Task 6
#Compulsory Task 1

print("Please enter three integers: ")
num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
num3 = int(input("Please enter the third integer: "))

Addition = num1 + num2 + num3
Subtraction = num1 - num2
Multiplication = num3 * num1
Division = Addition / num3
#Division = float(Addition / num3)

# The \n below adds a new line before printing the statement
print("\nThe sum of all three numbers are : ", Addition)    #using the print function with the comma means we do not have to convert the int to str.
#print("The sum of all three numbers are : " + str(Addition))
print("The subtraction of Num1 and Num2 is: ", Subtraction)
print("The multiplication of Num3 and Num1 is: ", Multiplication)
print("The division of the sum and Num3 is: ", Division)
