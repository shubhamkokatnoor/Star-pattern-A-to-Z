#Q) Make T to using star pattern
i=1
while i<=6:
    j=1
    while j<=7:
        if (((i==1) and (j>=1 and j<=7)) or ((i>=2 and i<=6) and (j==4))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1