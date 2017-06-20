"""
Problem 1 - Paying Debt Off In a Year (How much is left?)

Calculate the credit card balance after one year if
a person only pays the minimum monthly payment required
by the credit card company each month.

balance            - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

###
For each month, calculate statements on the monthly payment
and remaining balance. 

At the end of 12 months, print out the remaining balance
Two decimal digits of accuracy
###
"""


months = 12
balance = 42
monthlyPaymentRate = .04

annualInterestRate = .20
monthlyInterestRate = annualInterestRate / 12

for i in range(months):

    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interestAmount = unpaidBalance * monthlyInterestRate
    endingBalance = unpaidBalance + interestAmount
    balance = endingBalance

balance = round(balance, 2)
print ("Remaining balance:", balance)



# WITH DEBUGGING PRINT STATEMENTS 

# months = 12
# balance = 42
# monthlyPaymentRate = .04

# annualInterestRate = .20
# monthlyInterestRate = annualInterestRate / 12

# for i in range(months):
#     # print ("current balance:", balance)

#     minimumPayment = balance * monthlyPaymentRate
#     unpaidBalance = balance - minimumPayment
#     interestAmount = unpaidBalance * monthlyInterestRate
#     endingBalance = unpaidBalance + interestAmount
#     balance = endingBalance
    
#     # print ("minimum payment", minimumPayment)
#     # print ("unpaid balance", unpaidBalance)
#     # print ("interest amount", interestAmount)
#     # print ("ending balance:", balance)
#     # print ("___________________________________")
#     # print ()

# balance = round(balance, 2)
# print ("Remaining balance:", balance)
