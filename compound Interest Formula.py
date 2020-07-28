a = int(input("Enter the principle amount\n\n"))

b = int(input("Enter the time\n\n"))

c = float(input("Enter the rate of interest"))

e = 1 + (c/100)

for i in range(1,b+1):
    prod=1
    prod=prod*e

print(prod*float(a))
