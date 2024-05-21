def find_first_repeating_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            print(f"Character: {char}, Memory Address: {id(char)}")
            return char
        else:
            char_count[char] = 1
    return None
print(find_first_repeating_character("Hello world"))
