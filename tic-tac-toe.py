a = input("Enter player 1 symbol :- ")

if(a!=""):
    b = input("enter player 2 symbol :- ")

c=d=f=g=h=i=j=k=l=" "
counter = 9
if ( a!="" and b!="" and a!=b):
    while counter>0:
        if(counter%2!=0):
            s = "Player 1"
        else:
            s = "Player 2"    
        z=input("enter your choice {} :- ".format(s))
        if(counter%2==0):
            if(int(z)>9 or int(z)<1):
                print("Please enter choice in range 1-9")

            elif(z=="1" and c==" "):
                c=b
                counter = counter-1
            elif(z=="2" and d==" "):
                d=b
                counter = counter-1
            elif(z=="3" and f==" "):
                f=b
                counter = counter-1
            elif(z=="4" and g==" "):
                g=b
                counter = counter-1
            elif(z=="5" and h==" "):
                h=b
                counter = counter-1
            elif(z=="6" and i==" "):
                i=b
                counter = counter-1
            elif(z=="7" and j==" "):
                j=b
                counter = counter-1
            elif(z=="8" and k==" "):
                k=b
                counter = counter-1
            elif(z=="9" and l==" "):
                l=b
                counter = counter-1
            else:
                    print("{} is already occupied".format(z))
        elif(counter%2!=0):
            if(int(z)>9 or int(z)<1):
                print("Please enter choice in range 1-9")

            elif(z=="1" and c==" "):
                c=a
                counter = counter-1
            elif(z=="2" and d==" "):
                d=a
                counter = counter-1
            elif(z=="3" and f==" "):
                f=a
                counter = counter-1
            elif(z=="4" and g==" "):
                g=a
                counter = counter-1
            elif(z=="5" and h==" "):
                h=a
                counter = counter-1
            elif(z=="6" and i==" "):
                i=a
                counter = counter-1
            elif(z=="7" and j==" "):
                j=a
                counter = counter-1
            elif(z=="8" and k==" "):
                k=a
                counter = counter-1
            elif(z=="9" and l==" "):
                l=a
                counter = counter-1
            else:
                    print("{} is already occupied".format(z))        
            
        print("   |   |   ")
        print(" {} | {} | {} ".format(c,d,f))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(g,h,i))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(j,k,l))
        print("   |   |   ")

        if((c==a and d==a and f==a)or(g==a and h==a and i==a)or(j==a and k==a and l==a)or
           (c==a and g==a and j==a)or(d==a and h==a and k==a)or(f==a and i==a and l==a)or
           (c==a and h==a and l==a)or(f==a and h==a and j==a)):
               print("Player 1 wins")
               break
        if((c==b and d==b and f==b)or(g==b and h==b and i==b)or(j==b and k==b and l==b)or
           (c==b and g==b and j==b)or(d==b and h==b and k==b)or(f==b and i==b and l==b)or
           (c==b and h==b and l==b)or(f==b and h==b and j==b)):
               print("Player 2 wins")
               break    
else:
    print("Symbol of both players can't be same.")
