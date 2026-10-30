diviros = 0
try:
    if diviros == 0:
        raise RuntimeError("Error: Division by zero")
    else:
        result = 10/diviros
        print("Result : ", result)
except RuntimeError as e:
    print(str(e))
except:
    pass


print("Finally block executed")

name = "Peter"
try:
    if name == "Peter":
        name = name + " " + "parker"
        print(f"Name is : {name}", )
    else:
        print("No matched name exist.!")
        print(" Try Again")
except RuntimeError as e:
    print(str(e))
    
except:
    pass
