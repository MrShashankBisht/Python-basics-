list1 = ["string1 ",12]
print (list1)
tuple1 = (1,"hello",3.4)
print(type(tuple1))
print(type(list1))
_5 = 23
print(_5)
tuple2 = (tuple1,list1)
print(tuple2)
i=0
while(i < 3):
    print(tuple1[i])
    i=i+1
print 'out side the while loop and the ith value is ', i