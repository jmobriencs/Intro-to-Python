# John-Michael O'Brien
# w1890922
# CISP 300
# 2/27/20
# This program calculates the cost of purchasing a meal
# This program includes decisions and loops

# Lab 5-5 Yum Yum Burger Joint

# the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':   # loop to run program again
        totalBurger = 0     # reset variables
        totalFry = 0
        totalSoda = 0
        total = 0
        tax = 0
        subtotal = 0
        endOrder = 'no'
        while endOrder == 'no':     # loop to take in order
            print()     # prints a blank line
            print('Enter 1 for Yum Yum Burger')
            print('Enter 2 for Grease Yum Fries')
            print('Enter 3 for for Soda Yum')
            option = input('Enter now -> ')
            if option == '1':
                totalBurger = getBurger(totalBurger)
            elif option == '2':
                totalFry = getFry(totalFry)
            elif option == '3':
                totalSoda = getSoda(totalSoda)
            endOrder = input('Do you want to end your order? (yes/no): ')
    
        total = calcTotal(totalBurger, totalFry, totalSoda)
        printReceipt(total)
        
        endProgram = input('Do you want to end the program? (yes/no): ')
        print()     # prints a blank line

# this function calculates totalBurger
def getBurger(totalBurger):
    burgerCount = int(input('Enter the number of burgers you want: '))
    totalBurger = totalBurger + burgerCount * .99
    return totalBurger

# this function calculates totalFry
def getFry(totalFry):
    fryCount = int(input('Enter the number of fries you want: '))
    totalFry = totalFry + fryCount * .79
    return totalFry

# this function calculates totalSoda
def getSoda(totalSoda):
    sodaCount = int(input('Enter the number of sodas you want: '))
    totalSoda = totalSoda + sodaCount * 1.09
    return totalSoda

# this function calculates the total
def calcTotal(totalBurger, totalFry, totalSoda):
    subtotal = totalBurger + totalFry + totalSoda
    tax = subtotal * .06
    total = subtotal + tax
    return total

# this function prints the total
def printReceipt(total):
    print()     # prints a blank line
    print ('The total price is $',total)
    
# calls main
main()
