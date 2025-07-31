def is_armstrong_number(numbers):
    str_num = str(numbers)
    totle = sum(int(digit) ** len(str_num) for digit in str_num)
    arm = " + " .join(f"{digit}^{len(str_num)}" for digit in str_num)
    return print(totle == numbers, f"({totle} = {arm})" if totle == numbers else f"({numbers} != {numbers})")

is_armstrong_number(153)
is_armstrong_number(9474)
is_armstrong_number(123)