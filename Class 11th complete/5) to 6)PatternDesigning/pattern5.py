n = int(input("enter the number of row in your simple pattern = "))
print("\n")

for i in range(n):
    for k in range(i):
        print(" ", end="  ")
    for j in range(n-i,0,-1):
        print("*", end="  ")
    print("\n")


# -------------------Output of  the above code is given bellow ----------------------

# enter the number of row in your simple pattern = 5

# *  *  *  *  *
#    *  *  *  *
#       *  *  *
#          *  *
#             *