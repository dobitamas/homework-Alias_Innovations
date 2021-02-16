import copy
from characters import digits


def solve_number(number):
    result_number = ""

    temp_number = int(copy.copy(number))
    print("TEMP NUMBER: ", temp_number)
    while temp_number > 0:

        for key, value in digits:
            while temp_number >= key:
                result_number += value
                temp_number -= key
                print("RESULT NUMBER: ", result_number)
    if len(result_number) == 0:
        return None

    return result_number


def solve_all_numbers(numbers):
    result_numbers = []

    for number in numbers:
        if number is not None and int(number) < 4000:
            result_numbers.append(solve_number(number))
        else:
            result_numbers.append("Not valid")

    return result_numbers
