#Q) Make S to using star pattern
i=1
while i<=7:
    j=1
    while j<=7:
        if (((i==1 or i==4 or i==7) and (j>=3 and j<=6)) or ((i==2 or i==3) and (j==1)) or ((i==5 or i==6) and (j==7))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1