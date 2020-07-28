list = [5,-1,-1,1,2,3]

a = int(input("Enter a number\n\n"))


for val in list:
    if(list[val]==-1):
        list[val]=(list[val-1]+1)%7
        
print("\n\n")

print(list)


