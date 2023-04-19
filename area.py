a=int(input("enter the no.of sides"))
if(a==3):
    leng=int(input("enter the length"))
    ht=int(input("enter the height"))
    print("area of triangle is", 0.5*leng*ht)
elif(a==4):
    lt=int(input("enter the length"))
    bt=int(input("enter the breadth"))
    if(lt==bt):
        print("area of the square is", lt*lt)
    else:
        print("area of rectangle is", lt*bt)
else:
    print("area is not predictable")