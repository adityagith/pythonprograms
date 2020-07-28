# Normal naive method

list = [15,6,7,10,12,20,10,28,10]

a = 10

c=0

for val in list:
    if(val==a):
        c=c+1

print("Freqency of {} is {}".format(a,c))

# Second method by deleting all elements except a

for val in list:
    if(val!=a):
        list.delete(val)

print(len(list))

#First sort the elements then check for frequency


