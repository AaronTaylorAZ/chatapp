def fibonacci(n):
  if n == 0 or n == 1:
    #print (n)
    return n
  else:
   #print (fibonacci(n-1) + fibonacci(n-2))
    return (fibonacci(n-1) + fibonacci(n-2))
print(fibonacci(100))