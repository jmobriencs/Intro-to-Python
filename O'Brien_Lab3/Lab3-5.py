# John-Michael O'Brien
# w1890922
# CISP 300
# 2/13/20

# This program asks the user to enter an age, weight, and birth month.
# The program compares input data to the correct answers and only
# prints the appropriate responses.

# Guess the Secrets

# The main function
def main():
    age = getAge()
    weight = getWeight()
    birthMonth = getMonth()
    correctAnswers(age, weight, birthMonth)

# This function takes in age
def getAge():
    age = int(input('Enter your guess for age: '))
    return age

# This function takes in weight
def getWeight():
    weight = int(input('Enter your guess for weight: '))
    return weight

# This function takes in birth month
def getMonth():
    birthMonth = input('Enter your guess for the birth month: ')
    return birthMonth

# This function determines if guesses are correct
def correctAnswers(age, weight, birthMonth):
    if age <= 25:
        print('Congratulations, the age is 25 or less!')
    if weight >= 128:
        print('Congratulations, the weight is 128 or more!')
    if birthMonth == 'April':
        print('Congratulations, the birth month is April!')
  
# calls main
main()

        
    
    
