#Odd even lists

l=[]
l1=[]
l2=[]
s=int(input("Enter the size of the list:"))
for i in range(s):
    x=int(input("Enter list item:"))
    l.append(x)
for i in l:
    if(i%2==0):
        l1.append(i)
    else:
        l2.append(i)
print("Even elements list:",l1)
print("Odd elements list:",l2)