#area
import math
def arearetange ( ):
    l=input('enter the l value')
    b=input('enter the b value')
    return l*b
def areasqeure ( ):
    a=input('enter the a value')
    return a*a
def areatriangle ( ):
    b=input('enter the b value')
    h=input('enter the h value')
    return 1/2*b*h
def areacrcle ( ):
    r=input('enter the r value')
    return 22/7*r*r
def main():
    a=input("enter your choice 1:retange 2:sqeure 3:trianglr 4:crcle")
    if a==1:
        area=arearetange( )
    else:
        if a==2:
            area=areasqeure( )
        else:
             if a==3:
                 area=areatriangle( )
             else:
                 if a==4:
                     area=areacrcle( )
                 else:
                      print'rwong choice'
    print 'area is=',area
main()
