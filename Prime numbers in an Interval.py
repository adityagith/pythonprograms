a = int(input("Enter the first number\n"))

b = int(input("Enter the second number\n"))

def prime(n):
    if(n==2):
        print(n)
    else:
        for i in range(2,n):
            if(n%i==0):
                return
        else:
            print(n)
            return

print("The prime numbers bewteen {} and {} are:\n\n")

for i in range(a,b+1):
    prime(i)

print("\n\n")

