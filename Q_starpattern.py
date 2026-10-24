#Q) Make Q to using star pattern
i=1
while i<=10:
    j=1
    while j<=8:
        if (((i>=3 and i<=7) and (j==1 or j==6)) or ((i==2 or i==8) and (j==2 or j==5)) or ((i==1 or i==9) and (j==3 or j==4)) or ((i==7) and (j==4)) or ((i==9) and (j==7)) or ((i==10) and (j==8))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1