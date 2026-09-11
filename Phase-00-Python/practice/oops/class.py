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
