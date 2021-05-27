# John-Michael O'Brien
# w1890922
# CISP 300
# 3/7/20
# This program converts the flowcharts in Lab 6.2 to Python code

# Lab 6-3 Practicing for loops

# the main function
def main():

    # A Basic For loop
    print('I will display the numbers 1 through 5.')
    for num in [1, 2, 3, 4, 5]:
        print(num)
    print() # prints a blank line
    
    # The Second Counter code
    print('I will display the seconds 1 through 60.')
    for num in range (1, 61):
        print(num)
    print() # prints a blank line

    # The Accumulator code
    total = 0
    for counter in range(5):
        number = int(input('Enter a number: '))
        total = total + number
    print('The total is',total)
    print() # prints a blank line
                     
    # The Average Age code
    totalAge = 0
    averageAge = 0
    number = int(input('How many ages to enter: '))
    for counter in range(0, number):
        age = int(input('Enter age: '))
        totalAge = totalAge + age
    averageAge = totalAge / number
    print('The average age is',averageAge)
    
# calls main
main()
