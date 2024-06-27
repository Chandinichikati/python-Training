n=int(input())
s=str(n)
if s==s[::-1]:
    print("is palindrome")
else:
    print("not palindrome")
print(s)
