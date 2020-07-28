list = [12,35,9,56,24]


temp = list[0]

list[0] = list[len(list)-1]

list[len(list)-1] = temp

print(list)
