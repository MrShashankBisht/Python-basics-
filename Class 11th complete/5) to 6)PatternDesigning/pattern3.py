n = int(input("enter the number of row in your simple pattern = "))
print("\n")

for i in range(n,0,-1):
    for j in range(i):
        print("*", end="  ")
    print("\n")


# -------------------Output of  the above code is given bellow ----------------------

# enter the number of row in your simple pattern = 4

# *  *  *  *
# *  *  *
# *  *
# *