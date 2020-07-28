file1 = open("C:\\Users\\ADITYA\\Desktop\\Work\file1.txt","r")

string = file1.read()


for character in string:
    if(character!=' '):
        print(character)

        
file1.close()



#Adding Character


file1 = open("file1.txt","a")


name = "\nPathogen Chloroform Steve Stephen"


file1.write(name)


file1.close()
print("\n\n\n")

file1 = open("file1.txt")
file1.readline()
file1.close()


#C:\Users\ADITYA\Desktop\Work

# file.tell(),file.seek()
