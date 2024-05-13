# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

reply = int(input("Enter the number of people: "))
if reply > 8:
    print("You have to wait for a table")
else:
    print("Your table is ready")
# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
num = int(input("Enter the number you wish to check wether it is divisible by 10 or not: "))
if num % 10 == 0:
    print("The number is divisible by 10")
else:
    print("The number is not divisible by 10")