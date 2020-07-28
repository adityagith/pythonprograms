list1 = [2,-7,5,-64,-14]

p = 0

n = 0

for val in list1:
    if(val>=0):
        p = p + 1
    else:
        n = n + 1

print("pos = {} and neg = {}".format(p,n))


list2 = []
list3 = []

for val in list1:
    if(val>=0):
        list2.append(val)
    else:
        n = n + 1
        list3.append(val)

print("\n\n")

print("pos = {} and neg = {}".format(len(list2),len(list3)))



print(len(list2))
