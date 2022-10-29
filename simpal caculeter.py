#simpal calculeter
import math
def add():
    a=input('enter the a value')
    b=input('enter the b value')
    return a+b
def sub():
    a=input('enter the a value')
    b=input('enter the b value')
    return a-b
def mul():
    a=input('enter the a value')
    b=input('enter the b value')
    return a*b
def dev():
    a=input('enter the a value')
    b=input('enter the b value')
    return a/b
def main():
    ch=input("enter your choice1:add 2:sub 3:mul 4:dev")
    if ch==1:
        d=add()
    else:
        if ch==2:
            d=sub()
        else:
            if ch==3:
                d=mul()
            else:
                if ch==4:
                    d=dev()
                else:
                    print'rwong choice'
    print'calculet=',d
main()
