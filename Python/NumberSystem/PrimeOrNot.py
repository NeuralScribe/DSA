n = int(input("enter a number: "))
isPrime = True    
for i in range (2,n): 
    if n%i ==0: 
        isPrime = False 
if isPrime:
    print("The number is prime!")
else:
    print("The number is not prime!")