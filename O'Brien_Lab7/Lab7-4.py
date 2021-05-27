# John-Michael O'Brien
# w1890922
# CISP 300
# 3/14/20
# This program allows a student to enter their name and then asks them
# to solve ten random addition problems

# Lab 7-4 Math Test

# add libraries needed
import random

# the main function
def main():
    print()
    
    # initalize variables
    counter = 0
    studentName = 'NO NAME'
    averageRight = 0.0
    right = 0.0
    number1 = 0
    number2 = 0
    answer = 0.0

    # call to inputName
    studentName = inputName()

    # loop to run program again
    while counter < 10:
    
        # calls functions
        number1, number2 = getNumbers()
        answer = getAnswer(number1, number2)
        right = checkAnswer(number1, number2, answer, right)
        counter = counter + 1
        print() # prints a blank line

    averageRight = results(right, averageRight,)
    displayInfo(right, averageRight, studentName)

# this function gets the student name
def inputName():
    studentName = input('Enter student name: ')
    return studentName

# this function creates random numbers
def getNumbers():
    number1 = random.randint(1, 500)
    number2 = random.randint(1, 500)
    return number1, number2

# this function creates an addition problem
def getAnswer(number1, number2):
    print('What is the answer to the following equation?')
    print(number1)
    print('+')
    print(number2)
    answer = float(input('What is the sum: '))
    return answer

# this function checks the answer
def checkAnswer(number1, number2, answer, right):
    if answer == number1 + number2:
        print('Right')
        right = right + 1
    else:
        print('Wrong')
    return right

# this function calculates averageRight
def results(right, averageRight):
    averageRight = float(right) / 10
    return averageRight

# this function displays info and results
def displayInfo(right, averageRight, studentName):
    print('Information for student:',studentName)
    print('The number right:',right)
    print('The average right is %.2f'%averageRight,'or',averageRight * 100,'%')
    
# calls main
main()
