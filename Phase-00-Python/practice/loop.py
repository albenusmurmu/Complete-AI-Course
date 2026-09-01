# i = 1
# n = 5
# while i <= n:
#     print(i)
#     i += 1
# print("Ended..!")


# # Level 1: Basic Structure & Filtering
# # 1. The Multiples Filter
# # Concept: for loop with conditional logic.
# # Goal: Print all numbers from 1 to 50 that are divisible by 3 but skip any number that is also divisible by 5.

# print("Divisible by 3 but not 5  : ")
# for num in range(1,50):
#     if num % 3 == 0 and num % 5 != 0:
#         print(num, end=" ")

# print()

# # 2. The Interactive Guard
# # Concept: while loop for indefinite input validation.
# # Goal: Continuously ask the user to input a positive number. If they input a negative number or zero, print an error and ask again. Stop only when a valid positive number is entered.

# while True:
#     try:
#         user_input = int(input("Enter a number : "))
#         if user_input > 0 :
#             print(f'You entered right value: {user_input}')
#             break
#         else:
#             print("Please Enter a Positive Integer")
#     except ValueError:
#         print("Please Enter a valid code..!")
        
# while True:
#         user_name = input("Enter Your Name : ")
#         if user_name.isalpha():
#             print("name follow the rules")
#             break
#         else:
#             print("please enter valid name")
            
            
# # Skip the Vowels 
# # Concept : Interating strings with continue.
# # Goal : Take a string and print only its oconsonats. Skip every vowel using the continue statement.

# word = "PythonProgrammingLanguage"
# vowels = "AEIOUaeiou"
# print("Consonant Only : ")
# for char in word:
#     if char in vowels:
#         continue
#     else:
#         print(char, end=" ")
# print(" ")

# # Next Level : Accumulators & State Tracking
# # Connect : while loop with cumulative addition.
# # Goal : Given a maximum budget limit, process a list of expenses one by one. keep adding expence to your total until the next would exceed the limit. Stop immediately when that limit is threatened.
# budget_limit = 100
# expenses = [30,20,40,10,50]
# current_total = 0
# for ex in expenses:
#     if current_total + ex > budget_limit:
#         print(f'Stop Adding.! {ex} exceeding budget!')
#         break
#     current_total += ex
#     print(f'Add Expenses : {ex}.Total : {current_total}')
# print(f'Total Expenses : {current_total}')

# # next level 
# # Inventory search Safeguard 
# # Concept : Using loop else for "Not Found" scenarios.
# # Goal : Search an Inventory list for a specific item. If found, print a success message and break. If the loop finishes scanning without finding it, trigger the else block to log a "Restock Required" alert.

# inventory = ["laptop", "PC", "Mouse", "CPU", "Cable"]
# search_item = "PC"

# for items in inventory:
#     if search_item == items:
#         print(f'Item find in inventory : {inventory} {inventory.index(items)}')
#         break
#     else:
#         print("Item not exist in inventory Please try again..!")
        
# # next level
# # Alternating Sums
# # Concept : Dynamic loop arithematic using indexes.
# # Goal : Calculate the sum of a list where numbers at even indices are added, and numbers at odd idices are subtracted.  
# number = [2,5,6,7,1,8,9]
# total_namuber = 0

# for n in number:
#     if (n % 2 == 0):
#         total_namuber += n
#         print(f'Even Number : {total_namuber}')
#     else:
#         total_namuber -= n
#         print(f'Odd Number : {total_namuber}')
        
# print(f'Total Number : {total_namuber}')

# # For Loop
# # A kind of object not list
# for item in range(10):
#     print(item)
# for item in range(5, 10):
#     print(item)

# print(" ")
    
# prices = [20,10,30]
# total = 0
# for price in prices:
#     total += price
# print(total)

# # Nested loops

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
        
# print()

# normal loop
numbers = [5,2,5,2,2]
for number in numbers:
    print('X' * number)
    
# using nested loop
numbers = [5,2,5,2,2]
for x_count in numbers:
     output = ''
     for count in range(x_count):
         output +=  'X'
     print(output)
