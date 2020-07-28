file1 = open("file 2.txt")


a = []

b = []


for sentence in file1:
    a.append(sentence)

for sentence in a:
    for word in sentence:
        if(word!='\n'):
            b.append(word)

print(a)

b.reverse()

print(b)



file1.close()
