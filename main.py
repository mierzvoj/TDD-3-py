def roman(value):
    roman_map = {
        1: "I",
    }
    result = ""
    remainder = value

    for i in sorted(roman_map.keys(), reverse=True):
        if remainder > 0:
            multiplier = i
            roman_digit = roman_map[i]

            times = remainder // multiplier
            remainder = remainder % multiplier
            result += roman_digit * times
    print(result)
    return result


if __name__ == "__main__":
    inputnumber = 4
    roman(inputnumber)
