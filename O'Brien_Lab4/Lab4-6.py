# John-Michael O'Brien
# w1890922
# CISP 300
# 2/20/20
# This program calculates the tip, tax, and total price for a meal.
# The tip percentage depends on the meal price. The tax rate is 6%.
# The total is the meal price plus the tip plus the tax.

# This program uses functions and variables

# The main function
def main():
    print('Welcome to the meal calculator program')
    print() # prints a blank line
    mealPrice = inputMeal()
    tip = calcTip(mealPrice)
    tax = calcTax(mealPrice)
    total = calcTotal(mealPrice, tip, tax)
    printInfo(mealPrice, tip, tax, total)
    
# This function will input meal price
def inputMeal():
    mealPrice = input('Enter the meal price $')
    mealPrice = float(mealPrice)                                               
    return mealPrice

# This function will calculate tip
def calcTip(mealPrice):
    if mealPrice >= .01 and mealPrice <= 5.99:
        tip = mealPrice * .10
    elif mealPrice >= 6.00 and mealPrice <= 12.00:
        tip = mealPrice * .13
    elif mealPrice >= 12.01 and mealPrice <= 17.00:
        tip = mealPrice * .16
    elif mealPrice >= 17.01 and mealPrice <= 25.00:
        tip = mealPrice * .19
    else:
        tip = mealPrice * .22
    return tip
     
# This function will calculate tax at 6%
def calcTax(mealPrice):
    tax = mealPrice * .06
    return tax
    
# This function will calculate tip, tax, and the total cost
def calcTotal(mealPrice, tip, tax):
    total = mealPrice + tip + tax
    return total

# This function will print tip, tax, the meal price, and the total
def printInfo(mealPrice, tip, tax, total):
    print ('The meal price is $',mealPrice)
    print ('The tip is $',tip)
    print ('The tax is $',tax)
    print ('The total is $',total)
    
# calls main
main() 
