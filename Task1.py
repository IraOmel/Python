import sys

parametrs = sys.argv[1:] #get parametrs from command line

num1 = str(parametrs[0])
signh = str(parametrs[1])
num2 = str(parametrs[2])
command = num1 + signh + num2
result = eval(command)
print(result)