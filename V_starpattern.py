#Q) Make V to using star pattern
i=1 
while i<=5:
    j=1
    while j<=7:
        if (((i==1 or i==2) and (j==1 or j==7)) or ((i==3) and (j==2 or j==6)) or ((i==4) and (j==3 or j==5)) or ((i==5) and (j==4))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1