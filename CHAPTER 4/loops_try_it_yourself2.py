squares = [values ** 2 for values in range(1,11)]
print(squares)

numbers = [number for number in range(1,21)]
print(numbers)

millions = []
for n in range(1,1000001):
    millions.append(n)
# print(millions)
# for n in millions:
#     print(n)
print(min(millions))
print(max(millions))
print(sum(millions))

millionss = [numbers for numbers in range(1,1000001)]
print(sum(millionss))

odds = [odd for odd in range(1,20,2)]
for odd in odds:
    print(odd)

threemul = [ nums for nums in range(3,31,3)]
for nums in threemul:
    print(nums)

cubes = [cube**3 for cube in range(1,11)]
for i in cubes:
    print(i)

print(f"The first three cubes are",cubes[0:3])