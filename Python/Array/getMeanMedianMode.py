arr = list(map(int, input().strip().split()))
sum = 0
for a in arr:
    sum = sum+a 
print(sum/len(arr)) #mean
n = len(arr)
median = 0
if n % 2==0:
    median = (arr[(n//2)-1]+ arr[n//2])/2
else:
    median = arr[n//2]
print(median)

