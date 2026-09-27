#Q) make D to using star pattern
i=1
while i<=6:
     j=1
     while j<=7:
         if (((i==1 or i==6) and (j>=1 and j<=5)) or ((i>=2 and i<=5) and (j==1)) or ((i==2 or i==5) and (j==6)) or ((i==3 or i==4) and (j==7))):
             print("*",end="")
         else:
             print(" ",end="")
         j+=1
     print()    
     i+=1