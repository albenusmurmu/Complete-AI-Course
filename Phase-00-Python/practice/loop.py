i = 1
n = 5
while i <= n:
    print(i)
    i += 1
print("Ended..!")


# Level 1: Basic Structure & Filtering
# 1. The Multiples Filter
# Concept: for loop with conditional logic.
# Goal: Print all numbers from 1 to 50 that are divisible by 3 but skip any number that is also divisible by 5.

print("Divisible by 3 but not 5  : ")
for num in range(1,50):
    if num % 3 == 0 and num % 5 != 0:
        print(num, end=" ")

print()

# 2. The Interactive Guard
# Concept: while loop for indefinite input validation.
# Goal: Continuously ask the user to input a positive number. If they input a negative number or zero, print an error and ask again. Stop only when a valid positive number is entered.

while True:
    try:
        user_input = int(input("Enter a number : "))
        if user_input > 0 :
            print(f'You entered right value: {user_input}')
            break
        else:
            print("Please Enter a Positive Integer")
    except ValueError:
        print("Please Enter a valid code..!")