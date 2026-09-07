
Student_Names = ["Peter", "Pareek", "Albenus", "Murmu"]
for s_n in Student_Names:
    print(s_n)
first_name = Student_Names[1]
print("First Name : "+first_name)
first_name = "Albenus Murmu"
print("First Name01 : "+first_name)
print("Student_Name : "+ Student_Names[0]) # can't change in original list

# list methods

numbers = [2,4,6,9,20,30,10,4]
 # o/p = 4(if there are a value where we pass through numbers.index(20), Then it returns the index)
 # but the problem is that, if we haven't the value then it give us error value error, for avoid this we have solution
print(numbers.index(20))
print(4 in numbers) # It returns the TRUE and FALSE if number exist print it true, if not exist print FALSE

# count total similar values
print(numbers.count(4)) 

# Print None
# print(numbers.sort())
# here is the correct ver
numbers.sort()
print(numbers)
# copy() method
# insert
# append