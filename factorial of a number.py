a = int(input("Enter a number\n\n"))

def fact(n):
    fac=1
    for i in range(2,n+1):
        fac = fac*i

    print(fac)

fact(a)



def factorial(n): 
      if(n==1):
          return 1
      else:
          return n*factorial(n-1)
  
num = 6


factorial(num)


print(factorial(num))

