number=int(input())
actual = number
result = 0
while number > 0:
    rem = number % 10
    result += rem ** 3
    number //= 10
if actual == result:
    print("it is an armstrong number")
else:
    print("it is not armmstrong number")
