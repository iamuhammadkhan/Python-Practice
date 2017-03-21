calcValue1 = input('Please enter your first value ')

calcValue1 = int(calcValue1)

calcSign = input('Please enter an arthematic operator ')

calcValue2 = input('Please enter your second value ')

calcValue2 = int(calcValue2)

if calcSign == '+':
    print('Thank you, your result is: ', calcValue1 + calcValue2)
elif calcSign == '-':
    print('Thank you, your result is: ', calcValue1 - calcValue2)
elif calcSign == '*':
    print('Thank you, your result is: ', calcValue1 * calcValue2)
elif calcSign == '/':
    print('Thank you, your result is: ', calcValue1 / calcValue2)
else:
    print('Sorry you have entered invalid value or math operator, please try again')