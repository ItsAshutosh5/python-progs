list1=[1,2,3]

#Ways to print lists
print (list1)

print (*list1,sep=",")

[print (i,end=" ") for i in (list1)]

print("\n")
for x in range (len(list1)):
    print (list1[x],end=" ")
print("\n")

print (''.join(str(list1)))

print (' '.join(map(str,list1)))

print (str(list1[0:]))

print (str(list1[0:len(list1)]))




