#matrix addition
a=[]
b=[]
c=[]
d=[]
res=[]
result=[]
m=input('enter row number')
n=input('enter column number')
for i in range(0,m):
    for j in range(0,n):
        a.append(input('enter number'))
    c.append(a)
    a=[]
    print c
for i in range(0,m):
    for j in range(0,n):
        b.append(input('enter number'))
    d.append(b)
    b=[]
    print d
for i in range(0,m):
    for j in range(0,n):
        res.append(c[i][j]+d[i][j])
    result.append(res)
    res=[]
print'the added mateix is'
print result
