# /**
#  * Insertion sort is a basic sorting algorithm.
#  *
#  * Insertion sort iterates over an array, growing a sorted array behind the current location.
#  * It takes each element from the input and finds the spot, up to the current point,
#  * where that element belongs. It does this until it gets to the end of the array.
# */

# def insertSort(list):
#     for x in range(len(list)):
#         element = list[x]
#         for y in reversed(range(0, (x))):
#             if element <  list[y]:
#                 list[y + 1] = list[y]
#                 list[y - 1] = element
#             else:
#                 list[y] = list[x]
                
#     return list


# print(insertSort([1,4,2,5,6,3]))

def insertSort(my_list):
    for x in range(1, len(my_list)):
        element = my_list[x]
        y = x - 1

        while y >= 0 and element < my_list[y]:
            my_list[y + 1] = my_list[y]
            y -= 1

        my_list[y + 1] = element

    return my_list

# Example usage:
result = insertSort([1, 4, 2, 5, 6, 3])
print(result)

# element = list[x] / element = list[0] / element = 1
# look at the positions behind me
# if the element we are using is smaller than the variable we are looking at, we want to set our element behind that variable