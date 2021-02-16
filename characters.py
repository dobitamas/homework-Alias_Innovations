digits = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def get_number_from_roman(roman_digit):
    for int, roman in digits.items():
        if roman == roman_digit:
            return int

    return None


def get_roman_from_number(number):
    return digits.get(number, None)



