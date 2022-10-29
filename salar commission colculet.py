#salar commission colculet
sa=input('enter the amount')
if sa>=35000:
    rate=25
elif(sa>=25000)and(sa<35000):
    rate=20
elif(sa>=20000)and(sa<25000):
    rate=15
elif(sa>=10000)and(sa<20000):
    rate=12
elif(sa>=5000)and(sa<10000):
    rate=10
else:
    rate=0
commission=sa*rate/100.0
print'commission=',commission
d=sa+(sa*rate/100.0)
print'full amount=',d
    
