List1 = [10,20,30,40,50,60,70,80,90,100]
#slicing in list is same as slicing in string typelist 
#slicing(start:stop:step)

print(List1(0))

#checking is list is empity or not 
if not List1:
    print("this is empty ")
# Itteration over a list 
for (index, item) in enumerate(List1):
    print('The item in position {} is: {}'.format(index, item))