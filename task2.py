
for row in range(6):
    for ctr in range(6):
         if ctr==0 or ctr==5 or (row==ctr and (ctr>0 and ctr<5)):
             print("@" ,end=" ")
         else:
             print(end=" ")
    print()
for row in range(6):
    for ctr in range(5):
         if (ctr==0 or ctr==(4) and row!=0) or ((row==0 or row==3) and (ctr>0 and ctr<3)):
             print("**" ,end=" ")
         else:
             print(end=" ")
    print()
for row in range(6):
    for ctr in range(6):
         if ctr==0 or ctr==5 or (row==ctr and (ctr>0 and ctr<5)):
             print("@" ,end=" ")
         else:
             print(end=" ")
    print()
for row in range(6):
    for ctr in range(6):
         if ((row==0 or row==5) and (ctr!=0 and ctr!=5) or (ctr==0 or ctr==5) and (row!=0 and row!=5)):
             print("$" ,end=" ")
         else:
             print(end=" ")
    print()