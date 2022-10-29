#loop
i=1
sum=0.0
while i<=3:
    a=input("entar the mark")
    sum=sum+a
    i=i+1
percent=(sum/300)*100
if percent>=80:
    print"garad a"
    print"student first"
else:
    if percent>=70:
        print"garad b"
        print"student first"
    else:
        if(percent>=60)and(percent<70):
            print"garad c"
            print"student garad"
        else:
            if(percent>=40)and(percent<60):
                print"garad d"
                print"student garad"
            else:
                if percent<=40:
                    print"garad e"
                    print"fail"
                else:
                    print"fail"
