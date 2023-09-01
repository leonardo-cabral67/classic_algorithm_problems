def linear_search(list_to_find_element: list, value: float):
    list_length = len(list_to_find_element)
    for i in range(0, list_length):
        if(i == value):
            return True
    
    return False


numbers_list = range(0, 1025)

result = linear_search(numbers_list, 1029)
other_result = linear_search(numbers_list, 512)
print(result)
print(other_result)