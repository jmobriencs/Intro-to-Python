# John-Michael O'Brien
# w1890922
# CISP 300
# 4/17/20
# This program allows a user to enter a series of single digit numbers and
# the program displays the sum of all the single digit numbers in the string.

# Chapter 12: Sum of Digits in a String

# the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':
        userNumber = input('Please enter a series a single-digit numbers: ')
        sumOfDigits = getSumOfDigits(userNumber)
        printSum(userNumber, sumOfDigits)

        endProgram = input('Do you want to end program? (yes or no): ')
        while not(endProgram == 'yes' or endProgram == 'no'):
            print('Please enter a yes or no response')
            endProgram = input('Do you want to end program? (yes or no): ')
        print()

# the sum of digits function  
def getSumOfDigits(userNumber):
    sumOfDigits = 0
    for digitAsAString in userNumber:
        digitAsAnInt = int(digitAsAString)
        sumOfDigits = sumOfDigits + digitAsAnInt
    return sumOfDigits

# the print sum function
def printSum(userNumber, sumOfDigits):
    print('The sum of the digits in', userNumber, 'is', sumOfDigits)

# calls main
main()
