#Simple Calculator

x=float(input("Enter first number"))
y=float(input("Enter second number"))
add=x+y
sub=x-y
mul=x*y
div=x/y
mod=x%y
print("Addition:-",add)
print("Subtraction:-",sub)
print("Multiplication:-",mul)
print("Division:-",div)
print("Remainder:-",mod)


#Calculator using if elif

x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulous")
c=int(input("Enter your choice(1-5):"))
if(c==1):
    print(x+y)
elif(c==2):
    print(x-y)
elif(c==3):
    print(x*y)
elif(c==4):
    print(x/y)
elif(c==5):
    print(x%y)
else:
    print("Invalid choice")