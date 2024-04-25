# LEARNED MORE ABOUT HOW THE IN KEYWORD FUNCTIONS, WE LEARNED HOW TO REMEMBER DATA WHILE LOOKING THROUGH A DATA STRUCTURE
# /*
#  * Find the first item that occurs an even number of times in a list.
#  * Remember to handle multiple even-occurrence items and return the first one. 
#  * Return null if there are no even-occurrence items.
# */



def evenOccurence(list):
    mem = {}
    for num in list:
        if num in mem:
            mem[num] += 1
        else:
            mem[num] = 1
    # print(mem)
    for key in mem:
        if mem[key] % 2 == 0:
            return key
   
print(evenOccurence((9,2,9,2,7,3,8,4,5,8,4,1,4,3,7,0,7,1,8,9,3,7,9,2,2,4,3,1,2,6,7,2,0,3,8,6,9,3,6,2,4,7,5,7,0,8,7,7,6,4,5,1,4,4,3,3,6,6,5,1,1,5,4,9,8,0,9,4,7,1,0,1,3,8,2,0,2,4,2,7,1,5,2,1,3,1,3,9,2,1,7,7,1,0,3,5,5,4,3)))
print(evenOccurence((1,2,3,4,5)))

