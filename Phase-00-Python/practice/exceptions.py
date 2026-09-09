# exception trying to find the out error and resolve
#  Study about the types of error and how to handle them like valueErrors, IndentationError etc.

# 01
try:
    age = int(input('Enter yr age : '))
    print(f'{age} years old')
except ValueError:
    print('Please enter a valid age')
    
# 02
try:
    age = int(input('Enter yr age : '))
    income = int(input('Enter yr income : '))
    risk = income / age
    print(f'{risk} you can take the risk')
except ValueError:
    print('Please enter a valid age')
except ZeroDivisionError:
    print('age must be 1 or greater then 1')
    
