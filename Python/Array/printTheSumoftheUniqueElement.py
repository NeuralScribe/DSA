arr = list(map(int,input().strip().split()))
sum = 0
my_set = set()
for i in arr:
    my_set.add(i)
for j in my_set:
    sum += j
print(sum)
