print('hello frineds this is the program of dictionary')
rajan = "this is test of rajan";
friends = {'rajan':'rajan is my friend of xyz', 'rohan':'a programmer','ujwal': 'student',rajan:'this is for just fun'}
print(friends[rajan])
for key in friends:
    print(key ,":", friends[key])

Emp = dict({'name':'rajan','salary':100000,'age':24})
Emp1 = dict(zip(('name','salary','age'),('raj',100000,24)))
name = ['raj','rohan','himanshu']
age = [18,24,23]
salary = [10000,10000,10000]
emp = {'name':name,'age':age,'salary':salary}

print(Emp)
print(Emp1)
print(emp['name'])
Emp['dept'] = 'sales'
print(Emp)

del Emp['dept']
print(Emp)