#Q) Make L to using star pattern
i=1
while i<=5:
    j=1
    while j<=4:
        if (((i>=1 and i<=5) and (j==1)) or ((i==5) and (j>=2 and j<=4))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1