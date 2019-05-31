#To print grades

x=int(input("Enter the marks of the student:"))
if(x<=100 or x>=0):
        if(x>90 and x<=100):
            print("O")
        elif(x>80 and x<=90):
            print("A+")
        elif(x>70 and x<=80):
            print("A")
        elif(x>60 and x<=70):
            print("B+")
        elif(x>50 and x<=60):
            print("B")
        elif(x>40 and x<=50):
            print("C")
        elif(x>30 and x<=40):
            print("D")
        else:
            print("Fail")
else:
    print("Invalid input")    