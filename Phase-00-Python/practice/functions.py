# 01
def practice():
    print("Hello World01")
    print("Hello World02")
print("Hello World03")
practice()
print("Hello World04")
print("Hello World05")

#02 // Possitional Arguments
# here we pass the parameters
def user_data(name,email,password):
    print(f'User_Name : {name}')
    print(f'User_Email : {email}')
    print(f'User_Pass : {password}')
# here we pass the arguments
user_data("Peter","peter@gmail.com","Peter@123#")

#03 
# keyword arguments
def greet_user(first_name, last_name, company):
    print(f'Hey {first_name} {last_name} welcome to {company} !')

greet_user(last_name="Murmu",first_name="peter",company= "cloudy coders")


#04
# here we pass the possitional and keyword arguments 
# Important :- we cann't define first keyword argument and then possitional argument this gives us error
# Possitinal arguments and 
# keyword arguments
def greet_user(greet,first_name, last_name, company):
    print(f'{greet} {first_name} {last_name} welcome to {company} !')

greet_user("hello", last_name="Murmu",first_name="peter",company= "cloudy coders")
