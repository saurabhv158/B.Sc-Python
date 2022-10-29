#amount  simpal int amount
def rateint():
    if (amount<20000)&(time>=2):
        rate=6
    elif(amount>=20000)&(time>=2):
        rate=7
    elif(amount>=60000)&(time>=1):
        rate=8
    else:
        rate=4
    return rate
amount=input('enter the amount')
time=input('enter the time')
rate=rateint()
sint=(amount*time*rate)/100.0
fa=amount+sint
print'rate=',rate
print'simpal int=',sint
print'full amount=',fa
cint=amount*(1+rate/100.0)**time-amount
fa=amount+cint
print'rate=',rate
print'compaund int=',cint
print'full amount=',fa
