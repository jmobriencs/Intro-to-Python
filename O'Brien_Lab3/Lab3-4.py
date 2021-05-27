# John-Michael O'Brien
# w1890922
# CISP 300
# 2/13/20
# This program will demonstrate how to use decision 
# statements in Python.  

# This program determines if a bonus should be awarded

# The main function
def main():
    print('Welcome to the program')
    monthlySales = getSales()  # gets sales
    isBonus(monthlySales)   # function call to determine bonus
    isDayOff(monthlySales) # function call to determine day off
    
# This function gets the monthly sales
def getSales():
    monthlySales = float(input('Enter the monthly sales $'))
    return monthlySales

# This function determines if a bonus is awarded
def isBonus(monthlySales):
    if monthlySales >= 100000:
        print('You have earned a $5,000 bonus!!!')

#This function determines if all employees get a day off
def isDayOff(monthlySales):
    if monthlySales >= 112500:
        print('All employees get one day off!!!')

# calls main
main()
