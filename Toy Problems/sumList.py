# sumArray
# /*
#  * Given an array of numbers, calculate the greatest contiguous sum of numbers in it.
#  * A single array item will count as a contiguous sum.
#  *
#  * example 1: sumArray([1, 2, 3]); // => 6
#  * example 2: sumArray([1, 2, 3, -4]); // 6
#  * example 3: sumArray([1, 2, 3, -4, 5]); // 7
#  * example 4: sumArray([4, -1, 5]); // => 8
#  * example 5: sumArray([10, -11, 11]); // 11
#  */
def sumArray(list):
    largestsum = 0
    currentsum = 0
    i = 0
    while i < (len(list)):
        print("currentsum:", currentsum, "largestsum:" , largestsum)
        if (list[i] >= 0):
            currentsum += list[i]
        else:
            negsum = 0
            j = i
            while list[j] < 0:
                negsum += list[j]
                j += 1
            if abs(negsum) < list[j]:
                currentsum += negsum + list[j]
                i = j
            else:
                if currentsum > largestsum:
                    largestsum = currentsum
                currentsum = 0
                i = j - 1
        i += 1
    print(currentsum)
    if currentsum > largestsum:
        largestsum = currentsum
    return largestsum
        
        
print(sumArray([5,8,9,10,-200,4,5,7,1,-900,1,2,3,4,5]))


def max_contiguous_sum(arr):
    if not arr:
        return 0  # If the array is empty, the sum is 0
    
    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
arr = [5,8,9,10,-200,4,5,7,1,-900,1,2,3,4,5]
result = max_contiguous_sum(arr)
print("The greatest contiguous sum is:", result)