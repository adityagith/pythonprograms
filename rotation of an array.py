sample = [1,2,3,4,5,6,7]

print("List before rotation\n\n")

b = int(input("Enter the degree by which you want to rotate the array\n\n"))

def rotate(list,a):
    for i in range(0,a):
        sample.append(sample.pop(0))
    else:
        return

print("The rotated list is\n\n")

rotate(sample,b)

print(sample)

print("\n\n")
    
