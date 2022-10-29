#porgram to find sum of seier
def factocrial(n):
    fa=1.0
    for i in range(1,n+1):
        fa=fa*i
    return fa
n=input('enter the trams')
sum=1.0
for i in range(1,n+1):
    if i%2==0:
        sum=sum-(i/factorial(i))
    else:
        sum=sum+(i/factorial(i))
print'sum=',sum
