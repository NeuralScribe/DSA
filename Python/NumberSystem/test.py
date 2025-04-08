#print prime num in a range 1 to 100
sum = 0
for i in range(2, 101):
    #print a no is prime or not
    n = i
    isPrime = True
    for j in range(2, n):
        if n %j ==0:
            isPrime =False
    if isPrime:
        #print(i)
        sum = sum+i
print(sum, end = "")

    
