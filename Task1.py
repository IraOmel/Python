import sys

parameters = sys.argv[1:]  # get parameters from command line

num1 = str(parameters[0])
sign = str(parameters[1])
num2 = str(parameters[2])
try:
    command = num1 + sign + num2
    result = eval(command)
    print(result)
except ZeroDivisionError:
    print("Error")


