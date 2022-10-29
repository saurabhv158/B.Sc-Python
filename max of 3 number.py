#max of 3 number
num1=input("enter the number")
num2=input("enter the number")
num3=input("enter the number")
if(num1>num2)and(num1>num3):
    max=num1
elif(num2>num1)and(num2>num3):
    max=num2
else:
    max=num3
print'the max is',max
