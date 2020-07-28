list = [6,7,8,9]

b = (len(list)-(2))

print("\n\n")
def mono(array):
  if(list[0]<list[1]): 
    for i in range(1,b+1):
      if(list[i] > list[i+1]):
        print("None monotonic\n")
        return
      elif(list[i]<=list[i+1]):
        pass
    else:
      print("Monotonic")
      

mono(list)

print("\n\n")

print(list)
      
