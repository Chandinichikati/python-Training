n=int(input("enter a no.of terms:"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b