list = [ 1, 6, 3, 5, 3, 4 ]
a = 4
def present(arr,a):
    for val in list:
        if(val==a):
            print("Present")
            return
    else:
        print("Absent")
        return
present(list,4)
b = list.count(a)
if(b!=0):
    print("{} is present".format(a))
    
#hash table

