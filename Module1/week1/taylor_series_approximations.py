def factorial(number):
   if number == 0:
      return 1
   else:
      return number * factorial( number - 1)

def sin(x,n):
   total = 0
   for i in range(n):
      total = ((-1)**i) * (x**(2*i + 1))/factorial(2*i +1) + total
   return total

def cos(x,n):
   total = 0 
   for i in range(n):
      total = ((-1)**i) * (x**(2*i))/factorial(2*i) + total
   return total

def sinh(x,n):
   total = 0
   for i in range(n):
      total = (x**(2*i +1))/factorial(2*i +1) + total
   return total

def cosh(x,n):
   total = 0
   for i in range(n):
      total = (x**(2*i))/factorial(2*i) + total
   return total

if __name__ =="__main__":
   print(cos(x=3.14, n=10))
   print(sinh(x=3.14, n=10))
   print(sin(x=3.14, n=10))
   print(cosh(x=3.14, n=10))