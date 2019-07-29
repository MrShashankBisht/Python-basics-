n = int(input("enter the number of row in your simple pattern = "))
print("\n")
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for k in range(0,i):
        print("*", end=" ")
    print("\n")


# -------------------Output of  the above code is given bellow ----------------------

# enter the number of row in your simple pattern = 6

# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *