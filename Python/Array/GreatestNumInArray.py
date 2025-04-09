import sys 
arr = list(map(int,input().strip().split()))
GreatNum = max(arr)
#print( GreatNum)
secondGreat = -sys.maxsize #-1 #sys.maxsize korle value ta onk boro asbe
for a in arr:
    if a > secondGreat and a < GreatNum :
        secondGreat = a
print(secondGreat)
