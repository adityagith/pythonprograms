list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

list3 = []

c = max(list2)

a = len(list2)

for i in range(0,c+1):
    for j in range(0,a):
        if(list2[j]==i):
            list3.append(list1[j])

print(list3)


