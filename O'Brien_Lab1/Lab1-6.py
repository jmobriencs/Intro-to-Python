#John-Michael O'Brien
#w1890922
#CISP 300
#1/31/20
#This program calculates miles walked and calories lost for a specific day of the week.

dayWalked = input('Enter the day of the week you walked: ')
stepsTaken = int(input('Enter the number of steps taken that day: '))
milesWalked = (stepsTaken/2000)
caloriesLost = (stepsTaken/2000)*65
print ('You walked', milesWalked, 'miles on', dayWalked, 'and lost', caloriesLost, 'calories.')
