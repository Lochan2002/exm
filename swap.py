a=int(input("enter 1st num"))
b=int(input("enter 2nd num"))
c=int(input("enter 3rd num"))
t=a
x=b
y=c
if(a>b and a>c):
    if(c>b):
        c=t
        b=y
        a=x
    else:
        c=t
        a=y
elif(b>a and b>c):
    if(c>a):
        c=x
        b=y
        a=t
    else:
        c=x
        b=t
        a=y
elif(c>a and c>b):
    if(a>b):
        b=t
        a=x
else:
    print("the numbers may be same")
print(a,b,c)