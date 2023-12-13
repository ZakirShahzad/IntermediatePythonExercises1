def sum_common_keys(dict1, dict2):

    combined_dict = {}
    for key in dict1:
        if key in dict2:
            combined_dict[key] = dict1[key] + dict2[key]
    return combined_dict

# Test
dict_a = {'apple': 5, 'banana': 3, 'cherry': 7}
dict_b = {'apple': 3, 'banana': 4, 'date': 2}
print(sum_common_keys(dict_a, dict_b))  # Expected output: {'apple': 8, 'banana': 7}
