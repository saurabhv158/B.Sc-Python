#matrix multiplycation
a=[]
b=[]
temp1=[]
m=input('enter row number')
n=input('enter column number')
intresult=[]
result=[]
for i in range(0,m):
    for j in range(0,n):
        temp1.append(input('enter number'))
    a.append(temp1)
    temp1=[]
    print a
for i in range(0,m):
    for j in range(0,n):
        temp1.append(input('enter number'))
    b.append(temp1)
    temp1=[]
    print b
for i in range(0,len(a)):
    intresult=[]
    for j in range(0,len(b)):
        res=0
        for k in range(0,len(b)):
            res=res+a[i][k]*b[k][j]
        intresult.append(res)
    result.append(intresult)
    print result
print'the mult matrix is'
print result
