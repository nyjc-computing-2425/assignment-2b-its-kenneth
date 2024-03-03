num = input('Enter a number (decimal only): ')
# type your code here

dp = len(num) - 1 - num.index(".")

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
