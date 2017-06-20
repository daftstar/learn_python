"""
Problem 2 - Paying Debt Off In a Year - minimum payment - 0 balance

Calculate the fixed min monthly payment to zero out
credit card balancein one year

balance            - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
fixed_payment      - minimum monthly payment rate as a decimal

The monthly payment must be a multiple of $10
"""

months = 12
annualInterestRate = .20
monIntRate = annualInterestRate / months


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


fixed_pay_guess = 0
guess_increment = 10
balance = 3329
epsilon = .01


while calc_balance(balance, fixed_pay_guess) > epsilon:
    fixed_pay_guess += 10

print("Lowest Payment:", fixed_pay_guess)



# # With debug statements
# months = 12
# annualInterestRate = .20
# monIntRate = annualInterestRate / months


# def calc_balance(balance, monthlyPayment):
#     for i in range(months):
#         print ("Balance", balance)
#         unpaidBalance = balance - monthlyPayment
#         interestAmount = unpaidBalance * monIntRate
#         endingBalance = unpaidBalance + interestAmount
#         balance = endingBalance
#         print ("ending balance", endingBalance)
#         print ()
#     return (endingBalance)


# fixed_pay_guess = 0
# guess_increment = 10
# balance = 3329
# epsilon = .01


# while calc_balance(balance, fixed_pay_guess) > epsilon:
#     fixed_pay_guess += 10

# print("Lowest Payment:", fixed_pay_guess)