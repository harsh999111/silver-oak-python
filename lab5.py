'''list'''

a =[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i<5 :
        print(i)

'''list'''
a = [1, 1, 2, 3, 5, 5, 5, 6, 7, 8, 9]
print( [i for i in a if i < 10])


'''even and odd'''

a = int(input("enter first number:"))


if a%4==0:
    print("even number:")
if a%2==0:
    print("print even:")
else:
    print("odd number:")

