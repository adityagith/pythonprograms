file1 = open("file 2.txt")

       
for line in file1:
    for word in line.split(" "):
        if(word!='\n'):
            for character in word:
                print(character)

      
file1.close()
 
print("\n\nAlternate Method\n\n")

file1 = open("file 2.txt")

while(1):
    char = file1.read(1)
    if not char:
        break
    print(char)

file1.close()

