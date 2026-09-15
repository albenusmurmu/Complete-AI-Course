class Person:
    name = "Peter"
    age = 36
p1 = Person()
print(p1.name + " age is " + str(p1.age))
print("hello world")

# 02
class Point:
    def move(self, a,b):
        # print("move")
        return a + b
    def draw(self):
        print("draw")

p1 = Point()
print(p1.move(a=1,b=2))

# 03
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

p1 = Point()
p1.x = 10
p1.y = 20
print(p1.x, p1.y)
p1.move()

# 04
try:
    class Point:
        def move(self):
            print("move")

        def draw(self):
            print("draw")
    p1 = Point()
    p1.x = 10
    p1.y = 20
    print(p1.x, p1.y)
    p1.move()
    # here we will get the AttributeError 
    p2 = Point()
    print(p2.x)

except Exception as e:
    print(e)
    
    
# 05 constructors

class Cons:
    #  during object creation used def __new__(cls, *args, **kwargs):
    # self is used for current values
    # Object Initialization Phase
    def __init__(self, x, y):
        self.x = x
        self.y = y   
             
    def one(self):
        print("One")
        
    def two(self):
        print("two")
output = Cons(10,20)
output.x = 30
print(output.x, output.y)

