def encode_string(s):
    if not s:
        return ""
    encode = []
    current_char = s[0]
    count = 0
    for char in s:
        if char == current_char:
            count += 1
        else:
            encode.append(current_char + str(count))
            current_char = char
            count = 1
    encode.append(current_char + str(count))
    return ''.join(encode)


input_string = input("вводи строку: \n")
encode_string = encode_string(input_string)
print("строка:", encode_string)
