# input will prompt user for a bill amount at the command line
amount = float(input('Enter Total Amount: '))

tip_15 = amount * .15
tip_20 = amount * 0.2

rate = float(input('Enter Tip Rate (such as 0.15): '))

total = amount + tip_20


print('You should pay: %d' % (total))
