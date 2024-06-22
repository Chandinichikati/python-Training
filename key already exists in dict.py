d={}
for i in range(5):
    k=input("key:")
    v=input("value:")
    d[k]=v
k=input("enter key to search:")
if k in d:
    print("key is found")
else:
    print("key not found")
