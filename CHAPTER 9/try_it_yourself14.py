# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and print a message saying that
# any ticket matching these 4 numbers or letters wins a prize.

listnew = [6,5,8,9,10,1,2,5,4,3,'A','B','C','D','E']
from random import choice
selected = []
while len(selected)<4:
    s1 = choice(listnew)
    if s1 not in selected:
        selected.append(s1)
print('Any ticket matching the following number will win the lottery')
print(selected)

  