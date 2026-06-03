# Conditional Statements Problems 

"""
1. Leap Year Checker
Write a program that takes a year as input and determines whether it is a leap year.
A leap year is defined as follows:
- It is divisible by 4;
- However, if it is divisible by 100, it must also be divisible by 400 to be a leap year.
Example input 1 : 2000
Example output 1 : Leap year.
Example input 2 : 1900
Example output 2 : Not a leap year.
"""
year = int(input("Enter the year : "))
if year % 400 == 0 :
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0 :
    print("Leap year")
else:
    print("Not a leap year")

"""
2. Electricity Bill
Calculate the electricity bill based on units consumed.
For first 100 units, Rate is 5 Rs per unit.
For next 100 units, Rate is 8Rs per unit.
Above 200 units, Rate is 10Rs per unit.
Example input: 250
Example Output: 1800 
"""
units = int(input("Enter units: "))
if units<=100:
    bill = units * 5
elif units<=200:
    bill = (100 * 5) + ((units-100) * 8)
else:
    bill = (100 * 5) + (100 * 8) + ((units-200) * 10)
print("Bill = " , bill)



