def unique_elements(input_list):
    """
    Return a new list containing only the unique elements from the input list.
    
    Parameters:
    - input_list (list): List to extract unique elements from.

    Returns:
    - list: List of unique elements.
    """
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Test
test_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
print(unique_elements(test_list))  # Expected output: [1, 2, 3, 4, 5, 6, 7]
