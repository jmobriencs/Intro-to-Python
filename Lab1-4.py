#John-Michael O'Brien
#w1890922
#CISP 300
#1/31/20
#This program calculates how many credits are left until graduation.

studentName = input('Enter student name. ')
degreeName = input('Enter degree program name. ')
creditsDegree = int(input('Enter the number of credits needed for the degree. '))
creditsTaken = int(input('Enter the number of credits taken so far. '))
creditsLeft = creditsDegree - creditsTaken
print ('The student\'s name is', studentName)
print ('The degree program name is', degreeName)
print ('There are', creditsLeft, 'credits left until graduation. ')
