
def arithmetic(first_number, second_number, operation):
    try:
        if operation == '/':
            return first_number / second_number
        elif operation == '+':
            return first_number + second_number
        elif operation == '-':
            return first_number - second_number
        elif operation == '*':
            return first_number * second_number
        else:
            return "Неизвестная операция"
    except ZeroDivisionError:
        return print("На ноль делить нельзя!")





