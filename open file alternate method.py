file1 = open("file1.txt","r")


list = []

a = []


for each in file1:
    list.append(each)


for item in list:
    print (item,end="")

file1.close()

file1 = open("file1.txt")
print("\n\n")

a.append(file1.readline())
a.append(file1.readline())
a.append(file1.readline())
a.append(file1.readline())
a.append(file1.readline())
print(a)


file1.close()

b=[]

file1 = open("file1.txt")
print("\n\n")
while(file1.readline()):
    b.append(file1.readline())
print(b)
file1.close()
