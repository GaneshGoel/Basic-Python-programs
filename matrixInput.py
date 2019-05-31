#Matrix input

l=[]
s=int(input("Enter number rows of the matrix:"))
s1=int(input("Enter number of columns:"))
for i in range(s):
    l1=[]
    for j in range(s1):
        x=int(input("Enter item of matrix:"))
        l1.append(x)
    l.append(l1)
print(l)
    
#Using list comprehension
    
s=int(input("Enter number rows of the matrix:"))
s1=int(input("Enter number of columns:"))
l=[[int(input("Enter item:")) for i in range(s)]for j in range(s1)]
print(l)
