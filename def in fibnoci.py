#fibnoci of def
def fibnocii (n):
    if n==0:
        return 0
    else:
        if n==1:
            return 1
        else:
            if n>1:
                return(fibnocii(n-2)+fibnocii(n-1))
n=input('enter the n th terms')
d=fibnocii(n)
print d
