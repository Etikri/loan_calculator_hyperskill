import argparse
from math import ceil
from math import log
#test change
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
args = parser.parse_args()

for _ in range(1):
    # number of args check
    args_num = 0
    args_num += 1 if args.type else 0
    args_num += 1 if args.principal else 0
    args_num += 1 if args.interest else 0
    args_num += 1 if args.payment else 0
    args_num += 1 if args.periods else 0
    if args_num < 4 or args_num > 4:
        print("Incorrect parameters")
        break
    # interest inputed check
    if not args.interest:
        print("Incorrect parameters")
        break
    # negativity check
    if args.principal and args.principal < 0:
        print("Incorrect parameters")
        break
    if args.interest and args.interest < 0:
        print("Incorrect parameters")
        break
    if args.payment and args.payment < 0:
        print("Incorrect parameters")
        break
    if args.periods and args.periods < 0:
        print("Incorrect parameters")
        break
    # type inputed check
    if args.type != "diff" and args.type != "annuity":
        print("Incorrect parameters")
        break
    # diff payment section
    if args.type == "diff":
        # payment not inputed check
        if args.payment:
            print("Incorrect parameters")
            break
        # diff pay calculation
        total_paid = 0
        nominal_interest = args.interest / (12 * 100)
        for current_month in range(1, args.periods + 1):
            month_payment = (args.principal / args.periods
                             + nominal_interest * (args.principal - (args.principal * (current_month - 1)) / args.periods))
            r_month_payment = ceil(month_payment)
            total_paid += r_month_payment
            print(f"Month {current_month}: payment is {r_month_payment}")
        overpay = total_paid - args.principal
        print(f"\nOverpayment = {overpay}")
        break
    # annuity payment section
    if args.type == "annuity":
        principal = args.principal
        payment = args.payment
        interest = args.interest
        periods = args.periods
        nom_interest = interest / (12 * 100)
        if interest and payment and principal:
            pay_num = log((payment / (payment - nom_interest * principal)), 1 + nom_interest)
            periods = ceil(pay_num)
            year_check = periods % 12
            ending_month = "months" if 0 != year_check != 1 else "month"
            if periods > 12 and year_check != 0:
                years = periods // 12
                ending_y = "years" if years > 1 else "year"
                print(f"It will take {years} {ending_y} and {year_check} {ending_month} to repay this loan!")
            elif periods < 12:
                print(f"It will take {year_check} {ending_month} to repay this loan!")
            elif year_check == 0:
                years = periods // 12
                ending_y = "years" if years > 1 else "year"
                print(f"It will take {years} {ending_y} and {year_check} to repay this loan!")
        elif principal and interest and periods:
            payment = ceil(principal * ((nom_interest * (1 + nom_interest) ** periods) / ((1 + nom_interest) ** periods - 1)))
            print(f"Your monthly payment = {payment}!")
        elif interest and periods and payment:
            principal = payment / ((nom_interest * (1 + nom_interest) ** periods) / ((1 + nom_interest) ** periods - 1))
            print(f"Your loan principal = {int(principal)}!")
        overpay = ceil((periods * payment) - principal)
        print(f"Overpayment = {overpay}")