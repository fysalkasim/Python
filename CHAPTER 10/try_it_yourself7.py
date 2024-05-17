# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

print("type'q' to quit")

while True:
    try:
        num1 = input("First number: ")
        if num1 == 'q':
            break
        x = int(num1)
        num2 = input("Second number: ")
        if num2 == 'q':
            break
        y = int(num2)

    except ValueError:
        print("The entered value is not a numerical one")
    
    else:
        sum = x+y
        print(f"The sum of {x} and {y} is {sum}")
    
# 10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop
# so the user can continue entering numbers, even if they make a mistake and
# enter text instead of a number


print("type'q' to quit")

while True:
    try:
        num1 = input("First number: ")
        if num1 == 'q':
            break
        x = int(num1)
        num2 = input("Second number: ")
        if num2 == 'q':
            break
        y = int(num2)

    except ValueError:
        print("The entered value is not a numerical one")
    
    else:
        sum = x+y
        print(f"The sum of {x} and {y} is {sum}")