import math

# write your code here
print('What do you want to calculate?')
# choose a format
choice = input('type "n" - for count of months, \n'
               'type "a" - for annuity monthly payment, \n'
               'type "p" - for credit principal: \n')

if choice == 'n':
    principal = int(input('Enter the credit principal: \n'))
    payment = int(input('Enter monthly payment: \n'))
    interest = float(input('Enter credit interest: \n'))
    nominal_i = (interest / 100) / (12 * 1)
    periods = math.log((payment / (payment - nominal_i * principal)), 1 + nominal_i)
    conversion_year = periods // 12
    conversion_month = math.ceil(periods % 12)

    if conversion_month == 12:
        print('You need ' + str(int(conversion_year + 1)) + ' years to repay this credit!')
    else:
        print('You need ' + str(int(conversion_year)) + ' year and ' + str(conversion_month) + ' months to repay this credit!')


elif choice == 'a':
    principal = int(input('Enter the credit principal: \n'))
    payment = int(input('Enter count of periods: \n'))
    interest = float(input('Enter credit interest: \n'))
    nominal_i = (interest / 100) / (12 * 1)
    annuity = principal * (((nominal_i * ((1 + nominal_i) ** payment)) / (((1 + nominal_i) ** payment) - 1)))
    print('Your annuity payment = ' + str(math.ceil(annuity)) + '!')

elif choice == 'p':
    payment = float(input('Enter the monthly payment: \n'))
    months = int(input('Enter count of periods: \n'))
    interest = float(input('Enter credit interest: \n'))
    nominal_i = (interest / 100) / (12 * 1)
    principal = payment / (((nominal_i * ((1 + nominal_i) ** months)) / (((1 + nominal_i) ** months) - 1)))
    print('Your credit principal = ' + str(round(principal)) + '!')
