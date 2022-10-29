#fibroci
num=input("enter the no of terms")
fib1=0
fib2=1
count=2
print fib1,'\n',fib2
while count<=num:
    fib=fib1+fib2
    print fib
    count=count+1
    fib1=fib2
    fib2=fib
