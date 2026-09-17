import random

for i in range(3):
    # print(random.random())
    print(random.randint(10,20))
    
name = ["peter","parker","Andrew","Mosh"]
print(random.choice(name))

# task :- generate the random vlaues(2,4) like this

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        # return first,second # // always add tuple by default
        return (first,second)
    
dice = Dice()
print(dice.roll())
