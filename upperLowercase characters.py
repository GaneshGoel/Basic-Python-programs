#Calculate uppercase and lowercase characters

c=0
c1=0
x=input("Enter a string:")
for i in x:
    if(i.isupper()):
        c=c+1
    elif(i.islower()):
        c1=c1+1
print("Uppercase letters:",c)
print("Lowercase letters:",c1)