
def arithmetic(arg1, arg2, op):
    try:
        if op == '+':
            return arg1 + arg2
        elif op == '-':
            return arg1 - arg2
        elif op == '*':
            return arg1 * arg2
        elif op == '/':
            return arg1 / arg2
        else:
            return "Неизвестная операция"
    except ZeroDivisionError:
        return print("На ноль делить нельзя!")





