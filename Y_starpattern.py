#Q) Make Y to using star pattern
i=1
while i<=5:
    j=1
    while j<=5:
        if (((i==1) and (j==1 or j==5)) or ((i==2) and (j==2 or j==4)) or ((i>=3 and i<=5) and (j==3))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1