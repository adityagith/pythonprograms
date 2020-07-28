a = int(input("Enter a number to check its prime or not\n"))


if(a<=0):
    print("No")

elif(a==2):
    print("Yes")

elif(a>2):
    for i in range(2,a):
        if(a%i==0):
            print("Not a prime")
            break
    else:
        print("Prime")

