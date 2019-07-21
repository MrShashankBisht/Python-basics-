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


#  function to view matrics element in matrics way 
def ViewMatrics(mat):
    for i in  range(0,3):
        for j in range(0,3):
            print (mat[i][j] , end="   ")
        print("\n")

# function to adding b/w two matrics 

def addition(matrics1,matrics2):
    matrics3 = []
    for i in  range(0,3):
        temp = []
        for j in range(0,3):
            temp[j] = matrics1[i][j] + matrics2[i][j]
        matrics3.append(temp)
    return matrics3


# function to subtraction b/w two matrics 

def subtraction(matrics1,matrics2):
    matrics3 = []
    for i in  range(0,3):
        temp = []
        for j in range(0,3):
            temp[j] = matrics1[i][j] - matrics2[i][j]
        matrics3.append(temp)
    return matrics3
