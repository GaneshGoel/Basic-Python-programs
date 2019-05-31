# To map two lists into a dictionary
    
l1=[]
l2=[]
x=int(input("Enter size of lists:"))
print("Enter items of list 1:")
for i in range(x):
    d=int(input("Enter list item:"))
    l1.append(d)
print("Enter items of list 2:")
for i in range(x):
    e=int(input("Enter list item:"))
    l2.append(e)
y=dict(zip(l1,l2))
print(y)
