#Second largest number

l=[]
s=int(input("Enter the size of the list:"))
for i in range(s):
    x=float(input("Enter list item:"))
    l.append(x)
l.sort()
print("Second largest element",l[-2])
