n=int(input("Enter a number: "))
def fact(n):
   if n<2:
      return 1
   else:
      return n * fact(n-1)
result = fact(n)
print("Factorial of 5 is:",result)
