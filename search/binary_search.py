def binary_search(list_to_find_element, value):
    minor = 0
    major = len(list_to_find_element) - 1

    while minor <= major:
        middle = (major + minor) // 2
        print('loop')
        
        if value == list_to_find_element[middle]:
            return True
        elif value < list_to_find_element[middle]:
            major = middle - 1
        elif value > list_to_find_element[middle]:
            minor = middle + 1
        else:
            return True
    
    return False
        

list_to_find_element = list(range(1, 1025))
print(list_to_find_element[1023])
result = binary_search(list_to_find_element, 512)
print('result: ', result)  
