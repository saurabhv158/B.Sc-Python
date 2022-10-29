#prime or not
low=input("enter the min number")
high=input("entar the max number")
flag=0
for i in range (low,high+1):
    for num in range (2,i/2+1):
        if i%num==0:
            break
    else:
        print i
