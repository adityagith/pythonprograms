a = [81,52,45,10,3,2,96,96]

b = set(a)

print(b)

b = list(b)

b.sort()

b.reverse()

print(b)

d = int(input("Enter the value of n\n"))

for i in range(0,d):
    print(b[i],end=" ")
