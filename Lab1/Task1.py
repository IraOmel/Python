import sys

if len(sys.argv) < 4:
    print("Not enough parameters")
    sys.exit(1)
num1 = str(sys.argv[1])
sign = str(sys.argv[2])
num2 = str(sys.argv[3])

operation = ('+', '-', '*', '/')  # list with operations

if num1.isdigit() and num2.isdigit() and sign in operation:
    try:
        command = num1 + sign + num2
        result = eval(command)
        print(result)
    except ZeroDivisionError:
        print("Error")
else:
    print("Incorrect date")
    quit()
