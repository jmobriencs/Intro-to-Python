# John-Michael O'Brien
# w1890922
# CISP 300
# 2/20/20
# This program takes in monthly sales and percent increase of sales
# in order to determine the store and individual bonuses.

# Lab 4-5

# The main function
def main():
    monthlySales = getSales()   # call to get sales
    salesIncrease = getIncrease() # call to get sales increase
    storeAmount = storeBonus(monthlySales) # call to get store bonus
    empAmount = empBonus(salesIncrease) # call to get employee bonus
    printBonus(storeAmount, empAmount) # prints to screen
    
# This function gets the monthly sales
def getSales():
    monthlySales = float(input('Enter the monthly sales $'))
    return monthlySales
    
# This function gets the percent of increase in sales
def getIncrease():
    salesIncrease = float(input('Enter percent of sales increase: '))
    salesIncrease = float(salesIncrease)
    salesIncrease = salesIncrease / 100
    return salesIncrease

# This function determines the storeAmount bonus
def storeBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount


# This function determines the empAmount bonus
def empBonus(salesIncrease):
    if salesIncrease >= 5 / 100:
        empAmount = 75
    elif salesIncrease >= 4 / 100:
        empAmount = 50
    elif salesIncrease >= 3 / 100:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print('The store bonus amount is $',storeAmount)
    print('The employee bonus is $',empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print('Congrats! You have reached the highest bonus amounts possible!')

# calls main
main()

