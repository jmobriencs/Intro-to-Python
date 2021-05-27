# John-Michael O'Brien
# w1890922
# CISP 300
# 3/21/20
# This program calculates a phone bill for a cell phone user
# based on minutes used

# Lab 8-5 Cell Phone Minute Calculator

# the main function
def main():
    #declare local variables
    endProgram = 'no'
    while endProgram == 'no':
        minutesAllowed = 0
        minutesUsed = 0
        totalDue = 0
        minutesOver = 0

        #calls functions
        minutesAllowed = getAllowed(minutesAllowed)
        minutesUsed = getUsed(minutesUsed)
        totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)
        printData(minutesAllowed, minutesUsed, totalDue, minutesOver)

        #end of program/initialize loop
        endProgram = input('Do you want to end program? (yes or no): ')
        while not(endProgram == 'yes' or endProgram == 'no'):
            print('Please enter a yes or no')
            endProgram = input('Do you want to end program? (yes or no): ')
        print()
        
# this function gets how many minutes are allowed
def getAllowed(minutesAllowed):
    minutesAllowed = int(input('How many minutes are allowed: '))
    while minutesAllowed < 200 or minutesAllowed > 800:
        print('Please enter minutes between 200 and 800')
        minutesAllowed = int(input('How many minutes are allowed: '))
    return minutesAllowed

# this function gets how many minutes were used
def getUsed(minutesUsed):
    minutesUsed = int(input('How many minutes were used: '))
    while minutesUsed < 0:
        print('Please enter minutes of at least 0')
        minutesUsed = int(input('How many minutes were used: '))
    return minutesUsed 

# this function calculates cell phone bill based on minutes used
def calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver):
    if minutesUsed <= minutesAllowed:
        totalDue = 74.99
        minutesOver = 0
        print()
        print('You were not over your minutes for the month')
        print()
    else:
        minutesOver = minutesUsed - minutesAllowed
        extra = minutesOver * .2
        totalDue = 74.99 + extra
        print()
        print('You were over your minutes by',minutesOver)
        print()
    return totalDue, minutesOver

# this function displays info
def printData(minutesAllowed, minutesUsed, totalDue, minutesOver):
    print('--------MONTHLY USE REPORT--------')
    print()
    print('Minutes allowed were',minutesAllowed)
    print('Minutes used were',minutesUsed)
    print('Minutes over were',minutesOver)
    print('Total due is $',totalDue)
    print()

# calls main
main()
