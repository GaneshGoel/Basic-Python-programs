#largest number

l=[]
s=int(input("Enter the size of the list:"))
for i in range(s):
    x=float(input("Enter list item:"))
    l.append(x)
m=l[0]
for j in l:
    if(l[i]>m):
        m=l[i]
print("Largest number is:",m)
print("Index:",l.index(m))
