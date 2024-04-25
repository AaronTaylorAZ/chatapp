#LESSONS LEARNED: WRITE THE WAY WE THINK,RECURSION SHOULD HAVE 2 THINGS [A BASE CASE, AND A RECURSION CASE]

#1 number input
#count up to that number and print the output
#every time the number you would print need to see if its divisible by 3, print fizz, if its by 5, print buzz



def fizzbuzz(number):
    x = 1
    while x <= number:
        
        if x % 15 == 0:
            print ("fizzbuzz")
        elif x % 3 == 0:
            print ("fizz")
        elif x % 5 == 0:
            print ("buzz")
        else:
            print (x)

        x = x + 1
            
fizzbuzz(50)


def fibinacci(num):
    if num == 0 or num == 1:
     return num
    elif num > 1:
        return(fibinacci(num -1) + fibinacci(num -2))  
print(fibinacci(10))