#lcm of 2 number
a=input('enter the number')
b=input('enter the number')
if(a>b):
    max=a
else:
    max=b
while(1>0):
    if(max%a==0)and(max%b==0):
        lcm=max
        break
    else:
         max=max+1
print'the lcm=',lcm
