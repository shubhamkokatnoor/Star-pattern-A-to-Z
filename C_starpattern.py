#Q) make C to using star pattern
i=1
while i<=5:
     j=1
     while j<=5:
         if (((i==1 or i==5) and (j>=1 and j<=5)) or ((i>=2 and i<=4) and(j==1))):
              print("*",end="")
         else:
             print(" ",end="")
         j+=1
     print()
     i+=1