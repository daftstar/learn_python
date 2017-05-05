"""
PART 2
    Find minimum fixed monthly payment to off balance in 12 months
    NO Minimum Monthly Payment like in P1

    balance = outstanding baalnce on credit card
    annualInterestRate = annual interest rate as decimal

"""

line_break = ("\n" + "------------" + "\n")


def paying_off_debt(balance, annualInterestRate, monthlyPaymentAmount):

    # Initialize primary variables
    monthlyInterestRate = (annualInterestRate / 12)

    # Initialize first set of balance calculations
    new_unpaid_balance = (balance - monthlyPaymentAmount)
    new_interest_amt = (monthlyInterestRate * new_unpaid_balance)

    for i in range(0, 11):
        # print ("Month:", i)
        # print ("Current Balance: %.2f" % balance)   # 2 decimal float
        # print ("Fixed Min Payment:", monthlyPaymentAmount)
        # print ("Unpaid Balance:", new_unpaid_balance)
        # print ("Interest:", new_interest_amt)
        # print (line_break)

        balance             = new_unpaid_balance + new_interest_amt
        new_unpaid_balance  = balance - monthlyPaymentAmount
        new_interest_amt    = monthlyInterestRate * new_unpaid_balance

    return (new_unpaid_balance)


# print (paying_off_debt(4773, .2, 440))


def guess_min_balance(balance, annualInterestRate):
    count = 0
    monthlyPaymentAmount = 0
    zero_balance_monthlyPayment = paying_off_debt(balance, annualInterestRate, \
                                                  monthlyPaymentAmount)

    while zero_balance_monthlyPayment >= 0:
        # print (count)
        monthlyPaymentAmount += .01
        zero_balance_monthlyPayment = paying_off_debt(balance, annualInterestRate, monthlyPaymentAmount)
        count += 1
        # print ("Current Guess:", monthlyPaymentAmount)
        # print ("Amt Remaining: %.2f" % zero_balance_monthlyPayment)
        # print ()

    print ()
    # print (zero_balance_monthlyPayment)

    return ("Lowest Payment:", monthlyPaymentAmount)
    return (monthlyPaymentAmount)


print (guess_min_balance(3329, .2))
# print (guess_min_balance(320000, .2))


