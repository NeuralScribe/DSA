num = int(input())
sum =0
temp = num              #1234           #123     
n= len(str(num))
while temp>0:
    digit = temp%10     #1234/10 -> 4   #3
    sum += digit**n        #4              #3
    temp= temp//10      #123            #12
print(sum)
if sum ==num:
    print(True)
else:
    print(False)