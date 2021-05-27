# John-Michael O'Brien
# w1890922
# CISP 300
# 2/6/20
# This program demonstrates how to use variables and
# functions.

# This program uses function and variables

# the main function
def main ():
    print('Welcome to the variable program')
    print()    # prints a blank line
    
    name = inputName()
    print('Hello', name)
    age = inputAge()
    print('You are', age, 'years old')

# this function inputs name
def inputName():
    name = input('Enter your name: ')
    return name

# this function inputs age
def inputAge():
    age = int(input('Enter your age: '))
    return age
    
# calls main
main()
