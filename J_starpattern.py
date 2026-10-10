#Q) make J to using star pattern
i=1
while i<=7:
    j=1
    while j<=7:
        if (((i==1) and (j>=1 and j<=7)) or ((i>=2 and i<=6) and (j==4)) or ((i==7) and (j==2 or j==3)) or ((i==5 or i==6) and (j==1))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1