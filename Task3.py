sign = {'+', '-'}  # list of acceptable signs
number = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} # list of acceptable numbers


def check(index):  # return True/False if formula correct/incorrect,according EBNF syntax
    ind = True
    if ((formula[index] in sign and formula[index + 1] == '0') or
            (formula[index] in sign and formula[index + 1] in sign) or
            (formula[index] not in number and formula[index] not in sign)):
        ind = False
        return ind, None
    if index == len(formula) - 1:
        result = eval(formula)
        return ind, result
    return check(index + 1)  # recursion for check all parameters from input line


formula = str(input())
length = len(formula)
if (formula == ""):
    print((False, None))
    quit()
print(check(0))
