# John-Michael O'Brien
# w1890922
# CISP 300
# 4/4/20
# This program allows the user to input two years worth of energy
# bills and displays the monthly savings for going green. The user
# can also write to a file or read from a file (savings.txt)

# Lab 10-4 Going Green

#the main function
def main():
    endProgram = 'no'
    print()
    notGreenCost = [0] * 12
    goneGreenCost = [0] * 12
    savings = [0] * 12
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'Decemeber']
    option = 0
    while endProgram == 'no':
        print('Enter 1 to enter new data')
        print('Enter 2 to display data')
        print('Enter 3 to store data in file')
        print('Enter 4 to display data from file')
        option = int(input('Enter now -->'))
        print()
        # function calls
        if option == 1:
            getNotGreen(notGreenCost, months)
            getGoneGreen(goneGreenCost, months)
            energySaved(notGreenCost, goneGreenCost, savings)
        elif option == 2:
            displayInfo(notGreenCost, goneGreenCost, savings, months)
        elif option == 3:
            writeToFile(months, savings)
        elif option == 4:
            readFromFile(months, savings)
            
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
        print('Enter NOT GREEN energy costs for ',months[counter])
        notGreenCost[counter] = int(input('Enter now -->'))
        counter = counter + 1
    print()
    return notGreenCost

# the getGoneGreen function
def getGoneGreen(goneGreenCost, months):
    counter = 0
    while counter < 12:
        print('Enter GONE GREEN energy costs for ',months[counter])
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

# the writeToFile function
def writeToFile(months, savings):
    outFile = open('savings.txt', 'a')
    outFile.write('Savings' + '\n')
    outFile.write('--------' + '\n')
    counter = 0
    while counter < 12:
        outFile.write(months[counter] + '\n')
        outFile.write(str(savings[counter]) + '\n')
        counter = counter + 1
    outFile.close()

# the readFromFile function
def readFromFile(months, savings):
    inFile = open('savings.txt', 'r')
    str1 = inFile.read()
    print(str1)
    months = inFile.read()
    print(months)
    print()
    savings = inFile.read()
    print(savings)
    print()
    inFile.close()

# calls main
main()     
