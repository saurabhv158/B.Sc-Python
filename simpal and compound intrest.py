#simpal intrest and compound intrest
def sint(p,n,r):
    return (p*r*n)/100.0
def cint(p,n,r):
    return p*(1+r/100.0)**n-p
p=input('enter the principle')
r=input('enter the reat')
n=input('enter the time')
d=sint(p,n,r)
print'simpal int amount',d
d=cint(p,n,r)
print'compound int amount',d
