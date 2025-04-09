import sys # will provide access to some variable used or maintained by sys interpreter 
arr = list(map(int, input().strip().split()))
SmallNum = min(arr)
print(SmallNum)

# second smallest
secondSmallest = sys.maxsize #gives the largest element
for a in arr:
    if a < secondSmallest and a >SmallNum:
        secondSmallest = a 
print(secondSmallest)