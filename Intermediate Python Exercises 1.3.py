def letter_count(s):

    count_dict = {}
    for char in s:
        # Convert character to lowercase
        char_lower = char.lower()
        
        # Check if the character is a letter and not a space
        if char_lower.isalpha() and char_lower != ' ':
            count_dict[char_lower] = count_dict.get(char_lower, 0) + 1
    return count_dict

# Prompt user for input
user_input = input("Please enter a string: ")
print(letter_count(user_input))
