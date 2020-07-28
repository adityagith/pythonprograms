a = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

b = []

for val in a:
    if(a.count(val)>1):
        b.append(val)

print(b)

print("\n\n")

b = set(b)

b = list(b)

print(b)

b.clear()



        
