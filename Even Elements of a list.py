#Even elements of a list using list comprehension
    
l=[]
x=int(input("Enter size of list:"))
for i in range(x):
    a=int(input("Enter list item:" ))
    l.append(a)
l1=[i for i in l if i%2==0]
print(l1)
