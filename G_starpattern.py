#Q) make G to using star pattern
i=1
while i<=7:
    j=1
    while j<=6:
        if (((i>=2 and i<=6) and (j==1)) or ((i==1 or i==7) and (j>=2 and j<=6)) or ((i==6 or i==5) and (j==6)) or ((i==5) and (j==5 or j==4))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1