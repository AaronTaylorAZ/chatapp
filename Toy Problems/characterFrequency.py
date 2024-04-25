# /*
#  *  Write a function that takes as its input a string and returns an list of
#  *  tuples as shown below sorted in descending order by frequency and then by
#  *  ascending order by character.
#  *
#  *       :: Example ::
#  *
#  *  characterFrequency('mississippi') ===
#  *  [
#  *    ['i', 4],
#  *    ['s', 4],
#  *    ['p', 2],
#  *    ['m', 1]
#  *  ]
#  *
#  *       :: Example2 ::
#  *
#  *  characterFrequency('miaaiaaippi') ===
#  *  [
#  *    ['a', 4],
#  *    ['i', 4],
#  *    ['p', 2],
#  *    ['m', 1]
#  *  ]
#  *
#  *       :: Example3 ::
#  *
#  *  characterFrequency('mmmaaaiiibbb') ===
#  *  [
#  *    ['a', 3],
#  *    ['b', 3],
#  *    ['i', 3],
#  *    ['m', 3]
#  *  ]
#  *

#  */
from functools import cmp_to_key
    
def compare(item1, item2):
    if item1[1] < item2[1]: 
        return 1
    elif item1[1] > item2[1]:
        return -1
    elif item1[1] == item2[1] and item1[0] > item2[0]:
        return 1
    else:
        return 0

def characterFrequency(string):
    count = []
    for char in string:
        found = False
        for pair in count:
            if pair[0] == char:
                pair[1] += 1
                found = True
                break
        if not found:
            count.append([char, 1])
    return sorted(count, key=cmp_to_key(compare))
    
print(characterFrequency("mississippi"))
    
# def characterFrequency(s):
#     count = {}
#     for char in s:
#         count[char] = count.get(char, 0) + 1
#     return sorted(count, key=cmp_to_key)


# # Example usage:
# result = characterFrequency('mississippi')
# print(result)  # Output: [('i', 4), ('s', 4), ('p', 2), ('m', 1)]

# print(characterSort([["a", 1],["v", 1] ,["n", 1] , ["h", 1], ["l", 123123], ["z", 1]]))



# def compare(item1, item2):
#     if item1[1] < item2[1]: 
#         return -1
#     elif item1[1] > item2[1]:
#         return 1
#     elif item1[1] == item2[1] and item1[0] > item2[0]:
#         return -1
#     else:
#         return 0

# def characterFrequency(string):
#     count = []
#     for char in string:
#         found = False
#         for pair in count:
#             if pair[0] == char:
#                 pair[1] += 1
#                 found = True
#                 break
#         if not found:
#             count.append([char, 1])
#     x = sorted(count, key=lambda pair: (pair[1], pair[0]))
#     return x
    
# print(characterFrequency("mississippi"))