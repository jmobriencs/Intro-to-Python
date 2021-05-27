# John-Michael O'Brien
# w1890922
# CISP 300
# 5/3/20
# This program prompts a user to enter the name, type, and age of their pet.
# The data is stored in the object and uses the object's accessor methods to
# retrieve the pet's name, type, and age and displays the data to the screen.

# Chapter 14 - Pet Class

class Pet:
    def __init__(self, name, animalType, age):
        self.name = name
        self.animalType = animalType
        self.age = age

    def setName(self, name):
        self.name = name

    def setType(self, animalType):
        self.animalType = animalType

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getType(self):
        return self.animalType

    def getAge(self):
        return self.age


# the main function
def main():
    
    # prompt user to enter pet name, type, and age
    name = input('Enter pet name: ')
    animalType = input('Enter animal type: ')
    age = int(input('Enter pet age: '))
    print()

    pets = Pet(name, animalType, age)

    # display data stored in the fields
    print('Data added to records.')
    print()
    print('-----Data Entered-----')
    print('Pet Name:', pets.getName())
    print('Animal Type:', pets.getType())
    print('Age:', pets.getAge())
    
# calls main
main()
