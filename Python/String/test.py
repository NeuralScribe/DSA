arr = list(map(int,input().strip().split()))
sum =0
for a in arr:
    sum +=a
print(sum/len(arr))