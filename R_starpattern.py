#Q) Make R to using star pattern
i=1
while i<=9:
    j=1
    while j<=7:
        if (((i>=1 and i<=9) and (j==1)) or ((i==3 or i==4) and (j==2 or j==6)) or ((i==2 or i==5) and (j==3 or j==5)) or ((i==6) and (j==3)) or ((i==8) and (j==5)) or ((i==7) and (j==4)) or ((i==9) and (j==6))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1