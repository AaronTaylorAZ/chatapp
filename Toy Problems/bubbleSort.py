#  * Bubble sort is the most basic sorting algorithm in all of Computer
#  * Sciencedom. It works by starting at the first element of an array and
#  * comparing it to the second element; if the first element is greater than the
#  * second element, it swaps the two. It then compares the second to the third,
#  * and the third to the fourth, and so on; in this way, the largest values
#  * "bubble" to the end of the array. Once it gets to the end of the array, it
#  * starts over and repeats the process until the array is sorted numerically.
#  *
#  * Implement a function that takes an array and sorts it using this technique.
#  * Don't use JavaScript's built-in sorting function (Array.prototype.sort).
#  *
#  * QUERY: What's the time complexity of your algorithm? If you don't already
#  * know, try to intuit this without consulting the Googles.
#  *
#  * Extra credit: Optimization time! During any given pass, if no elements are
#  * swapped we can assume the list is sorted and can exit the function early.
#  * After this optimization, what is the time complexity of your algorithm?
#  *
#  * Moar credits: Do you need to consider every element every time you iterate
#  * through the array? Make it happen, boss. Again: Has the time complexity of
#  * your algorithm changed?

#  * Example usage:
#  * bubbleSort([2, 1, 3]); // yields [1, 2, 3]
def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def compare(index1, index2):
    if index1 >= index2:
        return index1
    else:
        return index2

def bubbleSort(list):
    for x in range(len(list) - 1):
        for x in range(len(list) - 1):
            if list[x]  > list[x + 1]:
                swap(list, x, (x + 1))
    return list

print(bubbleSort([12,34,5,6,77,12,12,34,5,6,77,12,12,34,5,6,77,12,12,34,5,6,77,12,5,12,123,12,31,23,123,12,312,31,2,4536,34,53,453,73,24,262,2,424]))