#armtrong
a=int(input("enter the number"))
t=a
sum=0
while(a!=0):
  rem=a%10
  sum=sum+rem*rem*rem
  a=a//10
if(sum==t):
  print("armstrong")
else:
  print("not armstrong")