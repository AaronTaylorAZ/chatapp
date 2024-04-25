import math
# /*
#  * Given a sorted list, find the index of an element
#  * using a binary search algorithm.
#  *
#  * Example usage:
#  *
#  * index = binarySearch((1, 2, 3, 4, 5), 4);
#  * print(index); // 3
#  * index = binarySearch((1, 2, 3, 4, 5), 8);
#  * print(index); // null

# def binarySearch(list,target):
#     firstInList = list[0]
#     lastInList = list[len(list) - 1]
#     mid = (firstInList + (lastInList - firstInList)) // 2
#     print(mid)
#     if target > mid:
#         while lastInList > target:
#             if target == lastInList:
#                 print(list[lastInList])
#                 break
#             else:
#                 lastInList -= 1
#     elif  target < mid:
#         while firstInList < target:
#             if target == firstInList:
#                 print(list[firstInList])
#                 break
#             else:
#                 firstInList += 1
#     else:
#         print(mid)
    
    

def binarySearch(list, target):
    min = 0
    max = len(list) - 1
    while min <= max:
        mid = math.floor((min + max) // 2)
        midValue = list[mid]
        if midValue == target:
            return mid
        elif midValue < target:
            min = mid + 1
        else:
            max = mid - 1

    return -1

    
print(binarySearch([1, 2, 3, 4, 5], 5))