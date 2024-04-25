# LEARNED TIME COMPLEXITY(efficency of some operation), We learned some SPACE COMPLEXITY(amount of memory used based on how many variables are present and what they contain)
# LEARNED REMEMBER WHAT PATCH UR PLAYING ON AND WHICH DATA STRUCTURES ARE BEST ON THE PATCH
# LEARNED NESTED LOOPS V SLOW
# LINEAR OR YOU'RE CRINGE UNLESS YOU CAN'T
# /**
#  * Write a function `f(a, b)` which takes two strings as arguments and returns a
#  * string containing the characters found in both strings (without duplication), in the
#  * order that they appeared in `a`. Remember to skip spaces and characters you
#  * have already encountered!
#  *
#  * Example: commonCharacters('acexivou', 'aegihobu')
#  * Returns: 'aeiou'
#  *
#  * Extra credit: Extend your function to handle more than two input strings.
#  */

def commonCharacters(stringOne, stringTwo):
    count = ""
    letterDict = {}
    for y in stringTwo:
        letterDict[y] = y
    for x in stringOne:
        if x in letterDict:
            count += x
            del letterDict[x]
    return count

print(commonCharacters('aacexivou', 'aegihobu'))
