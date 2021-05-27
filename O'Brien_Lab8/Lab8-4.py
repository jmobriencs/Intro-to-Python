# John-Michael O'Brien
# w1890922
# CISP 300
# 3/21/20
# This program takes in any number of test scores and calculates the average score

# Lab 8-4 Average Test Scores

# the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':
        totalScores = 0.0
        averageScores = 0.0
        score = 0
        number = 0
        counter = 1
        declareVariables(endProgram, totalScores, averageScores, score, number, counter)
        number = getNumber(number)
        totalScores = getScores(totalScores, number, score, counter)
        averageScores = getAverage(totalScores, number, averageScores)
        printAverage(averageScores)
        endProgram = input('Do you want to end the program? (yes/no): ')
        while not(endProgram == 'yes' or endProgram == 'no'):
            print('Please enter yes or no response only!')
            endProgram = input('Do you want to end the program? (yes/no): ')
        print()
        
# this module declares variables
def declareVariables(endProgram, totalScores, averageScores, score, number, counter):
    endProgram = 'no'
    totalScores = 0.0
    averageScores = 0.0
    score = 0
    number = 0
    counter = 1
    
# this module gets numbers
def getNumber(number):
    number = int(input('How many students took the test: '))
    while number < 2 or number > 30:
        print('Please enter a number between 2 and 30 - Try again!!!')
        number = int(input('How many students took the test: '))
    return number

# this module gets the scores
def getScores(totalScores, number, score, counter):
    for counter in range(0, number):
        score = int(input('Enter their score: '))
        while score < 0 or score > 100:
            print('Please enter a number between 0 and 100 - Try again!!!')
            score = int(input('Enter their score: '))
        totalScores = totalScores + score
    return totalScores

# this module gets the average
def getAverage(totalScores, number, averageScores):
    averageScores = totalScores / number
    return averageScores

# this module displays the average test score
def printAverage(averageScores):
    print('The average score is ',averageScores)

# calls main
main()
        
