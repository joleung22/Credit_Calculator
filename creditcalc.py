import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)
args = parser.parse_args()

try:
    if len(sys.argv) < 4:
        print('Incorrect parameters')

    """ Keys to variables (, :
        Dm = mth differentiated payment, Dm
        principal = credit principal, P
        nominal_i = nominal interest rate, i
        period = number of payments, n
        i = current period, m"""


    def overpayment(total_paid, principal):
        sum_paid = total_paid - principal
        print(f'Overpayment = {sum_paid}')
        return sum_paid


    def diff_payment(principal, period, interest):
        total_payment = 0
        nominal_i = interest / (12 * 100)
        for i in range(1, period + 1):
            dm = math.ceil((principal / period) + nominal_i * (principal - (principal * (i - 1))
                                                               / period))
            print('Month ' + str(i) + ': paid out ' + str(dm))
            total_payment += dm
        return total_payment


    def x_periods(principal, payment, interest):
        nominal_i = interest / (12 * 100)
        periods = math.ceil(math.log((payment / (payment - nominal_i * principal)), 1 + nominal_i))
        conversion_year = periods // 12
        conversion_month = math.ceil(periods % 12)
        total_payment = payment * periods
        if conversion_month == 12 or conversion_month == 0:
            print(f'You need {str(int(conversion_year))} years to repay this credit!')
        else:
            print(f'You need {str(int(conversion_year))} year and {str(conversion_month)} '
                  f'months to repay this credit!')
        return total_payment


    def x_payment(principal, periods, interest):
        nominal_i = interest / (12 * 100)
        annuity = math.ceil(principal * ((nominal_i * ((1 + nominal_i) ** periods))
                                         / (((1 + nominal_i) ** periods) - 1)))
        total_payment = periods * annuity
        print(f'Your annuity payment = {annuity}!')
        return total_payment


    def x_principal(payment, period, interest):
        nominal_i = interest / (12 * 100)
        principal = math.ceil(payment / ((nominal_i * ((1 + nominal_i) ** period))
                                         / (((1 + nominal_i) ** period) - 1)))
        print(f'Your credit principal = {principal}!')
        return principal


    if args.type == 'diff':
        total = diff_payment(args.principal, args.periods, args.interest)
        overpayment(total, args.principal)
    elif args.type == 'annuity' and args.interest > 0:
        if args.periods and args.principal:
            total = x_payment(args.principal, args.periods, args.interest)
            overpayment(total, args.principal)
        elif args.principal and args.payment:
            total = x_periods(args.principal, args.payment, args.interest)
            overpayment(total, args.principal)
        elif args.payment and args.periods:
            total = args.periods * args.payment
            print(f'Overpayment = {total - x_principal(args.payment, args.periods, args.interest)}')
    else:
        print('Incorrect parameters')
except:
    print('Incorrect parameters')