#factoral in def
def factoral(n):
    if n==1:
        return 1
    else:
        return n*factoral(n-1)
n=input('enter the n value')
d=factoral(n)
    print d
