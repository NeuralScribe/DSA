num = int(input())

temp = num
while temp > 0:
    digit = temp % 10
    print(digit)
    temp = temp // 10