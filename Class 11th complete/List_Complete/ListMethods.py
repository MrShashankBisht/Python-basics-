# # Append(value) this method will add value at the last of the list 
# print("here we will use some simple methods of list")
# option = "y"
# list1 = list();              #this is very first method to create a list type object but this list is empty at this time 
# while option == "y":               
#     value = int(input("Enter any number that you want ot add on the list :- "))
#     list1.append(value)                                             #we are adding value to the end of the list type variable list1
#     option = input("if you want to add more element in the list so plz enter y:-")      #here we are taking the option to continue the loop 

# print(list1)                #printing loop

# list2 = [20,30,4,239,32,23,23]              #creating list by second method

# some other way to creating list 
# name = list('hello')
# print(name)

# list2 = [1,2,3,4,5,6,7,8]
# name = "Shashank singh bisht"
# list2.append(name)              
# print(list2)

#Extend this is a method of the list in this we can extend the list 
# list2 = [1,2,3,4,5,6]
# list2.extend(range(3)) #the argument of the extend method is one and it should be iterable object 

# index(value, [startIndex], [stop Index]) this is a searching method of the list by this you can find any value by its value and find value by its location 
list2 = [1,2,3,4,5,6]
print(list2.index(4))           #it start counting the number from 0 

#insert method to insert the value at perticular location. insert method take 2 arguments first is the index(where to insert the value ), and second is value 
list2.insert(3,5)
print(list2)

#pop method will remove the lelement from the index
list2.pop(3)
print(list2)

#remove method take the value to remove, not the index of the value 
list2.remove(4)
print(list2)

# to reverse the current list we have a method which is reverse()
#reverse() – reverses the list in-place and returns None.
list2.reverse()
print(list2)

# count(value) – counts the number of occurrences of some value in the list.

print(list2.count(5))

# sort() – sorts the list in numerical and returns None.
list2.sort()
print(list2)