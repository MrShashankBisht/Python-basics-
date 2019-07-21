var = "this is global variable "
def createMatrics ():
    arr = []
    print("enter any number for creating your matrics ")
    for i in  range(0,3):
        temp = []
        for j in range(0,3):
            val = int(input("\n enter the value of position "+str(i) + str(j)+" : "))
            temp.append(val)
        arr.append(temp)
    return arr        


#  this is 
def ViewMatrics(mat):
    for i in  range(0,3):
        for j in range(0,3):
            print (mat[i][j] , end="   ")
        print("\n")
