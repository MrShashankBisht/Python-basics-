import math
area = float(input("Enter the area : "))
if area>0:
    radius = math.sqrt(area/math.pi)
    print("the radius of the circle is = ",radius)
else:
    print("Error: the are must be a positive integer")

# now let talk about elseif conditions

num = int(input("Enter a number "))
if num>89:
    letter = 'A'
elif num>79:
    letter = 'B'
elif num>69:
    letter = 'C'
else:
    Letter = 'F'

print('the letter grade is = ',letter)
