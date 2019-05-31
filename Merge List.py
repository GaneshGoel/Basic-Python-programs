#Merge two lists and sort it

l1=[]
l2=[]
l3=[]
l4=[]
x=int(input("Enter size of list 1:"))
y=int(input("Enter size of list 2:"))
print("\nEnter items of list 1")
for i in range(x):
    a=int(input("Enter list item:"))
    l1.append(a)
print("\nEnter items of list 2")
for i in range(y):
    b=int(input("Enter list item:"))
    l2.append(b)
l3=l1+l2
j=0 
while j in range(len(l3)):
    m=l3[0]
    s=len(l3)
    for i in range(s):
        if l3[i]<m:
            m=l3[i]
    l4.append(m)
    l3.remove(m)
print("Sorted list in ascending order:",l4)
