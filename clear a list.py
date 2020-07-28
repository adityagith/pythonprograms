list =  [1,2,3,4,5,6,7,8]


for i in range(0,8):
    list.pop()
    
    
print(list)


list =  [1,2,3,4,5,6,7,8]


print(list)


l=len(list)


print(l)


while(l!=0):
    list.remove(list[l-1])
    l=l-1

print(list)
