customary = {
    "name" : "Peter",
    "Age" : 21,
    "Company" : "Cloudy Coders"
}
print(customary["name"])
print(customary.get("Age"))
print(customary.get("company")) # when i used this .get method it returns me the "None" if it not match, so we can pass the random value also we can paas the random values ex:-
print(customary.get("Name", "Not Found "))
# for cs in customary:
#     print(cs)

#  Write a program to print the input number between 1 to 4

user_input = input(" Enter the number 1 to 4 : ")
digit_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for ch in user_input:
    output += digit_mapping.get(ch, "!") + " "
print(output)