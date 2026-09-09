# exception trying to find the out error and resolve
#  Study about the types of error and how to handle them like valueErrors, IndentationError etc.
try:
    age = int(input('Enter yr age : '))
    print(f'{age} years old')
except ValueError:
    print('Please enter a valid age')