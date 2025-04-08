#print a no is prime or not
n = int(input())
isPrime = True
for j in range(2, n):
    if n %j ==0:
        isPrime =False