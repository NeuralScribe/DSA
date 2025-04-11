#import sys
#arr = list(map(int,input().strip().split()))
num = int(input()) # 370
sum = 0             
temp = num          #371
n= len(str(num))
while temp>0:
    digit = temp %10
    sum += digit**n
    temp = temp//10
print(sum)