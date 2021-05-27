# John-Michael O'Brien
# w1890922
# CISP 300
# 3/28/20
# This program allows the user to input two years worth
# of data and displays the monthly savings for going green

# Lab 9-5 Going Green

#the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':
        # declare variables
        notGreenCost = [0] * 12
        goneGreenCost = [0] * 12
        savings = [0] * 12
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'Decemeber']

        # function calls
        getNotGreen(notGreenCost, months)
        getGoneGreen(goneGreenCost, months)
        energySaved(notGreenCost, goneGreenCost, savings)
        displayInfo(notGreenCost, goneGreenCost, savings, months)
    
        # program loop
        endProgram = input('Do you want to end program? (yes or no): ')
        while not (endProgram == 'yes' or endProgram == 'no'):
            print ('Please enter a yes or no response')
            endProgram = input('Do you want to end program? (yes or no): ')
        print()
    
# the getNotGreen function
def getNotGreen(notGreenCost, months):
    counter = 0
    while counter < 12:
        print('Enter NOT GREEN energy costs for '+months[counter])
        notGreenCost[counter] = int(input('Enter now -->'))
        counter = counter + 1
    print()
    return notGreenCost

# the getGoneGreen function
def getGoneGreen(goneGreenCost, months):
    counter = 0
    while counter < 12:
        print('Enter GONE GREEN energy costs for '+months[counter])
        goneGreenCost[counter] = int(input('Enter now -->'))
        counter = counter + 1
    print()
    return goneGreenCost

# the energySaved function
def energySaved(notGreenCost, goneGreenCost, savings):
    counter = 0
    while counter < 12:
        savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
        counter = counter + 1
    return savings

# the displayInfo function    
def displayInfo(notGreenCost, goneGreenCost, savings, months):
	counter = 0
	print('                      SAVINGS                    ')
	print('_____________________________________________________')
	print('SAVINGS      NOT GREEN      GONE GREEN      MONTH')
	print('_____________________________________________________')
	while counter < 12:
	    print('$',savings[counter],'       $',notGreenCost[counter],'         $',goneGreenCost[counter],'         ',months[counter])
	    counter = counter + 1
	print()
	
# calls main
main()     
