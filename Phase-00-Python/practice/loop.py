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
