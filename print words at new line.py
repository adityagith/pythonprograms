file2 = open("file 2.txt","r")

list = []

for each in file2:
    list.append(each)

print("Printing lines")

#print(list)

print("\n\n")

b = []
print("Words seperation\n\n")
for sentence in list:
    string = sentence
    b.append(string.split(" "))
    for item in b: # Item at b[0] always repeated
        for word in item:
            if(word!='\n'):
                print(word)
    b=[]#So words will not be repeated
    #del(b)

# For understaning purpose

#Upto here only
abc = "Hello people whats up"

a = []

a = abc.split(" ")

#print(a)


file2.close()

a=[]







print("\n\nAlternate Method")
file2 = open("file 2.txt","r")
while(file2.readline()):
    a.append(file2.readline())
file2.seek(0)
a.insert(0,file2.readline())
print(a)
b=[]
for item in a:
    b.append(item.split(" "))
print("\n\n")
print(b)
print("\n\n")
for sentence in b:
    for word in sentence:
        print(word)
file2.close()
