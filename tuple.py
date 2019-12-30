tuple1 = tuple('hello')
print(tuple1)
print(type(tuple1))

l=['w','o','r','l','d']
t1=tuple(l)
print(t1)

a=('a','b','c','d')
print(a[0])
tuple3=[4,5,6]
tuple2=(1,2,3,tuple3)

tuple3=tuple2
print(tuple3)

print(tuple3[0:4])
i=0
for temp in tuple3:
    if temp == 3:
        print(i)
    i=i+1

print(tuple2)
del tuple2
# print(tuple2)

print(max(tuple1))
print(min(tuple1))
print(tuple3.index(3))
print(tuple3.count(1))
print(len(tuple3))
testtup=(1,2,3,4,5,6,7,8,9)
for i in testtup[-1:-(len(testtup)+1):-1]:
    print(i)

