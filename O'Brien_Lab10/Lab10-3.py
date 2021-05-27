# John-Michael O'Brien
# w1890922
# CISP 300
# 4/4/20
# This program takes in pints of blood donated over a 7 hour period and
# calculates the average. The user can also write to a file or
# read from a file (blood.txt)

# Lab 10-3 Blood Drive

# the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':
        option = 0
        print()
        print('Enter 1 to enter in new data and store to file')
        print('Enter 2 to display data from the file')
        option = float(input('Enter now ->'))
        print()

        # declare variables
        pints = [0] * 7
        totalPints = 0
        averagePints = 0

        if option == 1:
            # function calls
            pints = getPints(pints)
            totalPints = getTotal(pints, totalPints)
            averagePints = getAverage(totalPints, averagePints)
            writeToFile(averagePints, pints)

        else:
            readFromFile(averagePints, pints)

        endProgram = input('Do you want to end program (Enter yes or no): ')
        while not (endProgram == 'yes' or endProgram == 'no'):
            print('Please enter a yes or no')
            endProgram = input('Do you want to end program? (Enter yes or no): ')
            
# the getPints function
def getPints(pints):
    counter = 0
    while counter < 7:
        pints[counter] = float(input('Enter pints collected: '))
        counter = counter + 1
    return pints
  
# the getTotal function
def getTotal(pints, totalPints):
    counter = 0
    while counter < 7:
        totalPints = totalPints + pints[counter]
        counter = counter + 1
    return totalPints

# the getAverage function
def getAverage(totalPints, averagePints):
    averagePints = float(totalPints / 7)
    return averagePints
    
# the writeToFile function
def writeToFile(averagePints, pints):
    outFile = open('blood.txt', 'a')
    outFile.write('Pints Each Hour' + '\n')
    counter = 0
    while counter < 7:
        outFile.write(str(pints[counter]) + '\n')
        counter = counter + 1
    outFile.write('Average Pints' + '\n')
    outFile.write(str(averagePints) + '\n\n')
    outFile.close()

# the readFromFile function
def readFromFile(averagePints, pints):
    inFile = open('blood.txt', 'r')
    str1 = inFile.read()
    print(str1)
    pints = inFile.read()
    print(pints)
    print()
    str2 = inFile.read()
    print(str2)
    averagePints = inFile.read()
    print(averagePints)
    print()
    inFile.close()
    
# calls main
main()
