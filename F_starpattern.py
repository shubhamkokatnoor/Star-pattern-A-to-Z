#Q) make F to using star pattern
i=1
while i<=7:
    j=1
    while j<=5:
        if (((i==1 or i==4) and (j>=1 and j<=7)) or ((i>=1 and i<=7) and (j==1))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1