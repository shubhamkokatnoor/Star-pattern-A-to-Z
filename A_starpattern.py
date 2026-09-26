# Q) make A to using star pattern 
i = 1
while i<=5:
    j = 1
    while j<=7:
        if (((i>=2 and i<=5) and (j==1 or j==7)) or ((i==1 or i==3) and (j>=2 and j<=6))):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1  