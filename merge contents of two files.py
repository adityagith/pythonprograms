file1 = open("file3.txt","a")


file2 = open("file1.txt")


file3 = open("file 2.txt")


file1.write(file2.read())


file1.write(file3.read())


file1.close()


file2.close()


file3.close()

print("Heres the merged data of the two files\n\n")


file1 = open("file3.txt","r")


print(file1.read())


file1.close()
