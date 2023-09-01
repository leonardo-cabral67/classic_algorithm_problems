def bubble_sort(list_to_be_sorted: list):
    list_length = len(list_to_be_sorted)
    for i in range(list_length-1):
        for j in range(list_length-1):
            current = list_to_be_sorted[j]
            next = list_to_be_sorted[j + 1]
            if  current > next:
                list_to_be_sorted[j], list_to_be_sorted[j+1] =  next, current

    return list_to_be_sorted


result = bubble_sort([-1,2, 1, 5, 6, 9, 11, 15, -3])
print(result)