#Task 6:
#Optional Task

print("Calculating the area of a triangle!")

side1 = float(input("Please enter the length of side1 of the triangle: "))
side2 = float(input("Please enter the length of side2 of the triangle: "))
side3 = float(input("Please enter the length of side3 of the triangle: "))

s = ((side1) + (side2) + (side3))/2
print("\n s =",s)

area = (s*(s-side1)*(s-side2)*(s-side3))
print("\nThe area of the triangle is: " + str(area))
