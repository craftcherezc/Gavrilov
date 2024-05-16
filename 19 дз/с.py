def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in s:
        value = roman_dict[char]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
            prev_value = value

    return result


def replace_roman_num_with_int(input_string):
    import re
    pattern = r'[IVXLCDM]+'
    replaced_string = re.sub(pattern, lambda x: str(roman_to_int(x.group())), input_string)
    return replaced_string


input_string = "В MMXIIII году в школе номер CXXIII выпустились XI классов."
output_string = replace_roman_num_with_int(input_string)
print(output_string)

