list = [70,11,20,4,100,100]

a = len(list)-1

for i in range(0,a+1):
    b = list.pop()
    list.insert(i,b)

print(list)

list.sort()

for i in range(0,a+1):
    b = list.pop()
    list.insert(i,b)

a = list[0]

b=1

c=a

if(list[1]==a):
    while(a==list[b]):
        b=b+1
    print(list[b])
else:
    print(list[1])


    
    
    
