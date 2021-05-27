# John-Michael O'Brien
# w1890922
# CISP 300
# 2/6/20
# This program calculates the county tax, state sales tax, and the
# total tax to be collected after a month of sales

# This program uses functions and variables

# the main function
def main():
    print('Welcome to the total tax calculator program')
    print() # prints a blank line
    totalsales = inputData()
    countytax = calcCounty(totalsales)
    statetax = calcState(totalsales)
    totaltax = calcTotal(countytax, statetax)
    printData(countytax, statetax, totaltax)
    
# this function will input monthly sales
def inputData():
    totalsales = input('Enter the total sales for the month $')
    totalsales = float(totalsales)
    return totalsales

# this function will calculate county tax at 2%
def calcCounty(totalsales):
    countytax = totalsales * .02
    return countytax
    
# this function will calculate state sales tax at 4%
def calcState(totalsales):
    statetax = totalsales * .04
    return statetax

# this function will calculate tip, tax, and the total cost
def calcTotal(countytax, statetax):
    totaltax = countytax + statetax
    return totaltax

# this function will print tip, tax, the meal price, and the total
def printData(countytax, statetax, totaltax):
    print('The county tax is $',countytax)
    print('The state tax is $',statetax)
    print('The total tax is $',totaltax)

# calls main
main()

