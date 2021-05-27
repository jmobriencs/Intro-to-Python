# John-Michael O'Brien
# w1890922
# CISP 300
# 4/22/20
# This program allows a user to enter a number and then will use
# recursion to calculate the sum.

# Chapter 13: Sum of Numbers Using Recursion

# recursion function
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)

num = int(input('Enter a number: '))
print('The sum is:',sum(num))
