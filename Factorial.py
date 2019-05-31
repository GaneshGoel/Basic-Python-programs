# Calculate factorial.

def fac(n):
    if n==0 or n==1:
        return 1
    elif n>1:
        return n*fac(n-1)
    else:
        print("Invalid input")
x=int(input("Enter an integer:"))
y=fac(x)
print(y)
