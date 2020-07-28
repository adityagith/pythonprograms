list = [12,10,5,6,52,36]

a = int(input("Enter a number to split the array\n\n"))


for i in range(0,a):
    list.append(list.pop(0))

print(list)

print("\n\n")
