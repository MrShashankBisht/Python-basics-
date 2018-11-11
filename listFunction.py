numbers = [1,3,2,5,4,7,6,8,9]
print(numbers.index(8))            #it will give u the index location of element 8

numbers.append(10)          # append the element 10 at the very last of the list 
print(numbers)
# now extending the number list
templist = [11,12,13]
print(templist)
numbers.extend(templist)
print(numbers)
#inserting the element

numbers.insert(4,4.5)
print(numbers)