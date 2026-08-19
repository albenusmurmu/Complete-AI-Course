course = "Python course for beginner's"
print(course)
courseOne = 'Python course for "Beginners"'
print(courseOne)

sendEmail = '''
HI $Sir;

Here is our first Email to you.


Thank you,
The Support Team

'''
print(sendEmail)

course = 'Hello World'
print(course[0], course[1], course[-1])
print(course[0:1])
print(len(course))

main = "Hello World"
print(main)
copy = main[:]
print(copy)

ex = "Hello Peter"
print(ex[-1])
print(ex[1:-1])


# Formating String

first_name = 'John '
last_name = 'Deo'
full_name = first_name + '[' + last_name+ '] is a coder'
print(full_name)
f_n = f'{first_name}[{last_name}] is a coder'
print(f_n)
print(f'{full_name} is a coder')


test_copy = f_n[:]
print(test_copy)
upper = test_copy.upper()
print(upper)
print(test_copy.lower())

# find method return index
ex = 'Hello peter'
print(ex.find('t'))
print(ex.find('peter'))
print(ex.replace('peter','Albenus Murmu'))

ex = 'python course'
# true and false like ex := course is in ex = true
print('course' in ex)

ex = 'PeTeR'
print(ex.title()) # o/p = Peter





