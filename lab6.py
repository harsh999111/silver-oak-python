'''for loop range'''

n=int(input("enter the number:"))
b=[]
for i in range(1,n+1):
    if  n%i==0:
        b.append(i)
print(b)