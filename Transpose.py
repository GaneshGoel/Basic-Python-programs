#Transpose

l=[]
s=int(input("Enter size:"))
for i in range(s):
    l1=[]
    for j in range(s):
        x=int(input("Enter item of matrix:"))
        l1.append(x)
    l.append(l1)
for i in range(s):
    print()
    for j in range(s):
        print(l[j][i])
