# 9-13. Dice: Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_die() that prints a random 
# number between 1 and the number of sides the die has. Make a 6-sided die and
# roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    '''Making a class named Die where we can use it for roll the die'''
    def __init__ (self,sides=6):
        self.sides = sides
    '''Creating a method called roll die'''
    def roll_die(self):
        max = self.sides
        print(randint(1,max))

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results2 = []
for roll_num in range(10):
    result = d10.roll_die()
    results2.append(result)
print("\n10 rolls of a 10-sided die:")
print(results2)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results3 = []
for roll_num in range(10):
    result = d20.roll_die()
    results3.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)
