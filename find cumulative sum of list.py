list1 = [10,20,30,40,50]

list2 = [4,10,15,18,20]

list3 = []

s = 0

a = len(list1)

for i in range(0,a):
    s = list1[i]+s
    list3.append(s)

print(list3)

s = 0

list3 = []

for i in range(0,a):
    s = list2[i]+s
    list3.append(s)

print(list3)
