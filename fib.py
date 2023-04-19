a=int(input("enter the number"))
b=0
c=1
if(a==0 or a==1):
    print("enter the value greater than 1")
else:
    print(b,end=" ")
    print(c,end=" ")
    for i in range(a-2):
        d=b+c
        print(d,end=" ")
        b=c
        c=d