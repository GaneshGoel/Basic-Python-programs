# Count frequency of words.
#Ist way
x=input("Enter a string:")
l=[]
x=x.lower()
l=x.split()
d={}
for i in l:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)


#IInd Way
counts = dict() 
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen'] 
counts.fromkeys(names)
for name in names : 
    counts[name] = counts.get(name, 0)+1 
print (counts)
