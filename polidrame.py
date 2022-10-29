#polidrame
st=list(raw_input('enter the string'))
l=len(st)
for i in range(0,l):
    if st[i]==st[l-i-1]:
        continue
    else:
        print 'not polidrame'
        break
else:
    print'it is a polidrame'
