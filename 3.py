#temprecher conversetion
x=input("print'1' to converet to 'f' & '2' for c")
if x==1:
    c=input("enter tempreter")
    f=(9.0/5.0)*c+32.0
    print f
else:
    f=input("enter tempreter")
    c=(f-32.0)*5.0/9.0
    print c
