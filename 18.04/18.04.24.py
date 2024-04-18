def find_longest_word(input_string):
    words = input_string.split()
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)


input_string = input("ВВОДИЛОВО СТРОкИ:")
longest_word, length = find_longest_word(input_string)
print(f"ДЛИНЕЙШЕЕ СЛОВО: {longest_word}, длина {length}")
