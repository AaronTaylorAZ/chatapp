# /**
#  * A prime number is a whole number that has no other divisors other than
#  * itself and 1. Write a function that accepts a number and returns true if it's
#  * a prime number, false if it's not.
#  */

def primeDivisor(primeNumber):
    i = 2
    while i < primeNumber:
        if primeNumber % i == 0:
            return False
        i += 1
    return True

    
print(primeDivisor(11123123))
