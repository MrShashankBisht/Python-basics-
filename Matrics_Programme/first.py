# 1)  break 
# 2) continue 
# 3) return

# break 

from math import sqrt
from matrics import *
print(__name__)

# def fuction1():
#     print(__name__)
    

# # fuction1()
# msg = maths.abc()
# print(msg)
matrics1 = createMatrics()
print("do you want to see your matrics if yes then press 0")
option = int(input())
if option == 0:
    ViewMatrics(matrics1)