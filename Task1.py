import sys

parameters = sys.argv[1:]  # get parameters from command line

num1 = str(parameters[0])
signh = str(parameters[1])
num2 = str(parameters[2])
command = num1 + signh + num2
result = eval(command)
print(result)
