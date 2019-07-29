n = int(input("enter the number of row in your simple pattern = "))
print("\n")
temp = n
for i in range(n):
    for j in range(0,temp):
        print(end=" ")
    temp -= 1
    for k in range(0,i+1):
        print("*", end=" ")
    print("\n")


# -------------------Output of  the above code is given bellow ----------------------

# enter the number of row in your simple pattern = 6

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *