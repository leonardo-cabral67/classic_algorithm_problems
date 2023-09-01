def selection_sort(list_to_be_sorted: list):
    list_lenght = len(list_to_be_sorted)
    for i in range(0, list_lenght):
        
        smaller_index = i
        
        for j in range(i + 1, list_lenght):
            if list_to_be_sorted[j] < list_to_be_sorted[smaller_index]:
                value_on_j_index = list_to_be_sorted[j]
                list_to_be_sorted[j] = list_to_be_sorted[i]
                list_to_be_sorted[i] = value_on_j_index
            

    return list_to_be_sorted


result = selection_sort([10, 9, 11, 8, 7, 6, 5, 4, 3, 1, 2])
print(result)
        