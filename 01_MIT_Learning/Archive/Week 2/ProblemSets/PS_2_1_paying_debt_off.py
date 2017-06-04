"""
Write program to calculate:
    Credit card balance after 1 year if person
    pays off only miminum monthly payment / year.

    balance = outstanding card balance 
    annualInterestRate = annual interest rate as decimal
    monthlyPaymentRate = minimum monthly payment rate as decimal

    For each month, calculate statements on monthly payment
    and remaining balance. Print at 2 decimal points of accuracy
    e.g. 813.41 vs. 813.414199...

    - Monthly Interest Rate     = Annual Interest Rate / 12
    - Min. Monthly Payment      = Min Month Payment * Previous Balance
    - Monthly Unpaid balance    = Previous Balance - Min Monthly Payment
    - Updated Balance / month   = 
            Monthly Unpaid Bal + (Mon. Int. Rate * Monthly Unpaid Balance)

"""


# annualInterestRate = .18
# monthlyPaymentRate = .02
# monthlyInterestRate = round((annualInterestRate / 12), 4)

# balance = 5000
# new_current_balance = round(balance, 2)

# new_min_payment = round((new_current_balance * monthlyPaymentRate), 2)
# new_unpaid_balance = round((new_current_balance - new_min_payment), 2)
# new_interest_amt = round(monthlyInterestRate * new_unpaid_balance, 2)

# for i in range(12):
#     print ("Month:", i)
#     print ("Current Balance:", new_current_balance)
#     print ("Minimum Payment:", new_min_payment)
#     print ("Unpaid Balance:", new_unpaid_balance)
#     print ("Interest:", new_interest_amt)
#     print ("\n" + "------------" + "\n")

#     new_current_balance = round((new_unpaid_balance + new_interest_amt), 2)
#     new_min_payment = round((new_current_balance * monthlyPaymentRate),2)
#     new_unpaid_balance = round((new_current_balance - new_min_payment), 2)
#     new_interest_amt = round((monthlyInterestRate * new_unpaid_balance), 2)


balance = 484
annualInterestRate = .2
monthlyPaymentRate = .04
line_break = ("\n" + "------------" + "\n")



def paying_off_debt(balance, annualInterestRate, monthlyPaymentRate):

    monthlyInterestRate = (annualInterestRate / 12)

    new_current_balance = balance

    new_min_payment = (new_current_balance * monthlyPaymentRate)
    new_unpaid_balance = (new_current_balance - new_min_payment)
    new_interest_amt = (monthlyInterestRate * new_unpaid_balance)

    for i in range(0,12):
        # print ("Month:", i)
        # print ("Current Balance: %.2f" % new_current_balance)   # 2 decimal float
        # print ("Minimum Payment:", new_min_payment)
        # print ("Unpaid Balance:", new_unpaid_balance)
        # print ("Interest:", new_interest_amt)
        # print (line_break)

        new_current_balance = (new_unpaid_balance + new_interest_amt)
        new_min_payment = (new_current_balance * monthlyPaymentRate)
        new_unpaid_balance = (new_current_balance - new_min_payment)
        new_interest_amt = (monthlyInterestRate * new_unpaid_balance)

    return ("Remaining Balance: %.2f" % new_current_balance + "\n")


print (paying_off_debt(balance, annualInterestRate, monthlyPaymentRate))
