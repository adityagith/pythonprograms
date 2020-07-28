print("To check Armstrong number\n\n")

a = input("Enter a number:\n\n")

b =len(a) #To calculate length of strings as it would give us number of digits


c = int(a)



def armstrong(a):

    sum = 0
    
    for val in a:
        
        sum = sum + pow(int(val),b)

    if(sum==c):
        print("Armstrong number")
    else:
        print("Non Armtrong")

armstrong(a)
