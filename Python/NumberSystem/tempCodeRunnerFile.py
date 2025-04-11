 digit = temp%10     #1234/10 -> 4   #3
    sum += digit**n        #4              #3
    temp= temp//10      #123            #12
print(sum)