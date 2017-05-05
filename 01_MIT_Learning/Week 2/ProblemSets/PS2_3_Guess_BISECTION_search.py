"""
PART 3
    Find minimum fixed monthly payment to off balance in 12 months
    
    balance = outstanding balance on credit card
    annualInterestRate = annual interest rate as decimal

"""



"""
THIS REDUCES CALC TIME BY USING LOWER BOUND

def guess_min_balance(balance, annualInterestRate):

    count = 0
    epsilon = 0.011
    monthlyInterestRate = annualInterestRate / 12

    mp_lower = balance / 12

    zero_balance_monthlyPayment = paying_off_debt(balance, annualInterestRate, mp_lower)

    while zero_balance_monthlyPayment >= epsilon:

        print (count)
        zero_balance_monthlyPayment = paying_off_debt(balance, annualInterestRate, mp_lower)
        mp_lower += .01
        count += 1
        # print ("Current Guess:", mp_lower)
        # print ("Amt Remaining: %.2f" % zero_balance_monthlyPayment)
        # print ()

    print ()
    print (zero_balance_monthlyPayment)

    return ("Lowest Min Month Payment:", mp_lower)


# print (guess_min_balance(1200, .2))
print (guess_min_balance(320000, .2))
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

        balance                 = new_unpaid_balance + new_interest_amt
        new_unpaid_balance      = balance - monthlyPaymentAmount
        new_interest_amt        = monthlyInterestRate * new_unpaid_balance

    return (new_unpaid_balance)


# # USING BISECTIONAL SEARCH
# def guess_min_balance(balance, annualInterestRate):

#     epsilon = .01
#     monthlyInterestRate = annualInterestRate / 12

#     high = (balance * ((1 + monthlyInterestRate) ** 12)) / 12
#     low = balance / 12
#     ans = (low + high) / 2.0

#     final_bal = paying_off_debt(balance, annualInterestRate, low)

#     while
#     print ("Lowest Min Month Payment:", low)

# # print (guess_min_balance(1200, .2))
# print (guess_min_balance(3329, .2))


balance = 1000
originalBalance = balance

annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
lowestBalance =.01 # Error margin e.g. $0.01
count = 0

# Keep testing new payment values until the balance is +/- lowestBalance
while abs(balance) > lowestBalance:
    # Reset the value of balance to its original value
    balance = originalBalance
    # Calculate a new monthly payment value from the bounds
    payment = (upperBound - lowerBound) / 2 + lowerBound

    # Test if this payment value is sufficient to pay off the entire balance in 12 months
    for month in range(12):
        balance = (balance - payment) * (1 + monthlyInterestRate)
        print ("Month:", count)
        print ("Balance for end of year:", balance)
        print ("Payment:", payment)
        print ("\n ------------------ \n")
        count += 1

    # Reset bounds based on the final value of balance
    print ("#####################")
    count = 0
    if balance > 0 < lowestBalance:
        # If the balance is too big, need higher payment so we increase the lower bound
        lowerBound = payment
        print ("Too big of a balance remaining. Using higher payment")
    else:
        # If the balance is too small, we need a lower payment, so we decrease the upper bound
        upperBound = payment
        print ("Too much of a negative balance, using lower payment")

# When the while loop terminates, we know we have our answer!
print ("Lowest Payment:", round(payment, 2))


