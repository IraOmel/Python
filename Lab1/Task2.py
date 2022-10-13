import sys

parameters = sys.argv[1:]
operation = str(parameters[0])
num1 = str(parameters[1])
num2 = str(parameters[2])

sign = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/'}  # dictionary with operations
if operation not in sign:
    print("Unknown operation")
    quit()
if num1.isdigit() and num2.isdigit():
    try:
        command = num1 + sign[operation] + num2
        result = eval(command)  # get result of operation
        print(result)
    except ZeroDivisionError:
        print("Error")
