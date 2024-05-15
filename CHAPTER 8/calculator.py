def calculator(a,b):
    '''It calculates addition, substraction, multiplication and division'''
    operation = input("Enter the operation (+,-,*,/): ")
    num1 = int(a)
    num2 = int(b)
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    else:
        print(num1 / num2)