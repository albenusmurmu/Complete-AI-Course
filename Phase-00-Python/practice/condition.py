is_hot = False
is_cold = False

if is_hot:
    print('Today is hot day')
elif is_cold:
    print('Today is cold day ')
else:
    print('Today is Normal Day')

# TASK
from math import floor
house_price = 1000000
has_goodCredits = True
if has_goodCredits:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print(f'Down payment: ${floor(down_payment)}')

# Logical Operators
# If applicants has high income AND good credit Eligible for loan
is_high_income = True
is_good_credit = True
if is_high_income and is_good_credit:
    print('Eligible for Loan')
else:
    print('Not eligible for Loan')

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for Loan")
else:
    print("Not eligible for Loan")

# Comparison Operator
# temperature = 30
temperature = int(input("Enter temperature in Celsius : "))

if temperature >= 30 :
    print(f'Its Hot day {temperature}!')
elif temperature < 10 :
    print(f'Its cool day {temperature}!')
else:
    print(f'It is either Hot nor Cold {temperature}!')

name = "pe"
if len(name) < 3:
    print("name is too short please enter valid name or add more than 3 characters")
elif len(name) > 50:
    print("name is too long please enter valid name or add below than 50 characters")
else:
    print("name is valid")

weight = int(input("Weight : "))
unit = input("(L)bs or (K)g : ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'You are converted to {converted} kg')
elif unit.upper() == "K":
    converted = weight / 0.45 # // = this GIVE THE INT VALUE BUT / THIS GIVE THE FLOAT VALUE
    print(f'You are converted to {converted} lbs')
else:
    print("Please enter a valid unit")






