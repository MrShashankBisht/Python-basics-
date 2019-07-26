# for<variable> in range(<an integer expression>):
    #statement -1
    #statement -2
    #statement --
    #----
    #----
    #statement -n

for eachPass in range(10):
    print("\n \tit's alive ! yes It's alive! \n")
print("Noe out of life ")


# traversing the contents of a data sequence 
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for number in list1:
    print ("the first number is == ", number)

# you can take lower and upper limit from user like this 

upperlimit = int(input("Enter the upper limit"))
lowerlimit = int(input("Enter the lower limit "))
for userloopnum in range(lowerlimit,upperlimit):
    print(" -- > ", userloopnum)



