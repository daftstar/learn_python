"""
Problem 2 - Paying Debt Off In a Year - minimum payment - 0 balance

Calculate the fixed min monthly payment to zero out
credit card balancein one year

balance            - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
fixed_payment      - minimum monthly payment rate as a decimal

The fixed_payment must result in a $0 balance +- $0.01 cents

"""

# Balance Details
balance = 99999
annualInterestRate = .18

months = 12
monIntRate = annualInterestRate / months


# Bisection Search Details
# narrow the low and high by using real world implications
# low, we could pay off the balance if we divided into 12 chunks
# high, pay off only at end of year, accounting for interest, divided into 12 chunks.
low = balance / months
high = (balance * ((1 + monIntRate) ** months)) / months
fixed_pay_guess = ((low + high) / 2)
epsilon = 0.1


# CORE LOGIC TO CALCULATE FINAL BALANCE
def calc_balance(balance, monthlyPayment):
    """ 
    balance        = integer starting balance
    monthlyPayment = integer guess of monthly payment

    expected output:
    the lowest fixed payment required to generate
    an ending balance < 0
    """

    for i in range(months):
        unpaidBalance = balance - monthlyPayment
        interestAmount = unpaidBalance * monIntRate
        endingBalance = unpaidBalance + interestAmount
        balance = endingBalance
    return (endingBalance)


# CONDITIONAL LOGIC.
# As long as the resulting guess is greater or less than 0.1 of 0,
# continue refining the mid-point guess.
#
# If the mid-point guess is too high (results in overpayment),
#   then set the upper bounds to the current value of the mid-point guess.
# Otherwise, we've underpaid and the balance is too high:
#   set the lower bounds to the current value of the mid-point guess.
# Then change the midpoint guess to the new average of upper + lower bounds.

def final_balance():
    if balance <= epsilon:
        return epsilon
    else:
        





while abs(calc_balance(balance, fixed_pay_guess)) > epsilon:
    if calc_balance(balance, fixed_pay_guess) < epsilon:
        high = fixed_pay_guess
    else:
        low = fixed_pay_guess
    fixed_pay_guess = ((low + high) / 2)

print ("Lowest Payment:", round(fixed_pay_guess, 2))
