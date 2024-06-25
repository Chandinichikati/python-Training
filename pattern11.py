n=int(input())
sp=n-1
for i in range(1,n+1):
    for sp in range(i,n):
        print(" ",end="")
    for j in range(1,i*2):
        print(j,end="")
    print()
    sp=sp-1
