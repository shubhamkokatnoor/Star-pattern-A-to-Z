#Q) Make Z to using star pattern
i=1
while i<=4:
    j=1
    while j<=4:
        if (((i==1 or i==4) and (j>=1 and j<=4)) or ((i==2) and (j==3)) or ((i==3) and (j==2))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1