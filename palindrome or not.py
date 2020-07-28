s = input("Enter a string to check its palindrome or not\n\n")

def pal(str):
    b = list(str)
    a = list(str)
    a.reverse()
    p = len(a)
    for i in range(0,p):
        if(b[i]!=a[i]):
            print("Non palindrome")
            return
        else:
            print("Palindrome")
            return
pal(s)

def pali(str):
    i=-1
    a = list(str)
    b = len(a)
    b=b/2
    while(i!=-1*(b)):
        if(a[i]!=a[i+1]):
            print("Not palindrome")
            return
        else:
            i=i-1;
    else:
        print("Palindrome")
        return
    
pali(s)






