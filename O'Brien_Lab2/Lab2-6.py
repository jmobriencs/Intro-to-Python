# John-Michael O'Brien
# w1890922
# CISP 300
# 2/6/20
# This program calculates a 20% tip and 6% tax on a meal price.
# The user will enter the meal price and this program will calculate the
# tip, tax, and the total.
# The total is the meal price plus the tip plus the tax.

# This program uses functions and variables

# the main function
def main():
    print('Welcome to the meal calculator program')
    print() # prints a blank line
    mealprice = input_meal()
    tip = calc_tip(mealprice)
    tax = calc_tax(mealprice)
    total = calc_total(mealprice, tip, tax)
    print_info(mealprice, tip, tax, total)
    
# this function will input meal price
def input_meal():
    mealprice = input('Enter the meal price $')
    mealprice = float(mealprice)
    return mealprice

# this function will calculate tip at 20%
def calc_tip(mealprice):
    tip = mealprice * .20
    return tip
    
# this function will calculate tax at 6%
def calc_tax(mealprice):
    tax = mealprice * .06
    return tax
    
# this function will calculate tip, tax, and the total cost
def calc_total(mealprice, tip, tax):
    total = mealprice + tip + tax
    return total

# this function will print tip, tax, the meal price, and the total
def print_info(mealprice, tip, tax, total):
    print ('The meal price is $',mealprice)
    print ('The tip is $',tip)
    print ('The tax is $',tax)
    print ('The total is $',total)
    
# calls main
main()
    
