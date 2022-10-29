#hcf in 2 number
a=input('enter the number1')
b=input('enter the number2')
if (a>b):
    min=b
    for i in range(1,min+1):
        if (a%i==0)and(b%i==0):
            gcd = i
            continue
else:
    min=a
    for i in range(1,min+1):
        if (a%i==0)and(b%i==0):
            gcd = i
            continue
print 'the hcf =',gcd
