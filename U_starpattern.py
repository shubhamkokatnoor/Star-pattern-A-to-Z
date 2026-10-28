#Q) Make U to using star pattern
i=1
while i<=7:
    j=1
    while j<=7:
        if (((i>=1 and i<=6) and (j==1 or j==7)) or ((i==7) and (j>=3 and j<=5))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1