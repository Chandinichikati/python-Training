n=int(input())
sp=0
for i in range(n,0,-1):
    for sp in range(i,n):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print( )
    sp=sp+1
