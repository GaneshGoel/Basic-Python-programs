# Check whether a string is pangram or not

x=input("Enter a string:")
z=x.lower()
s=set(z)
l1=[]
for i in s:
    if i.isalpha():
        l1.append(i)
l2=set(l1)
if len(l2)==26:
    print("Pangram")
else:
    print("Not pangram")
