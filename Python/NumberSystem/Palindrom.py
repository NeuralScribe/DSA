def is_palindrome(num):
    temp = num
    rev = 0
    while num > 0:  #23
        dig = num % 10 
        rev = rev * 10 + dig # -> 230+2
        num = num // 10  
    return temp == rev

num = int(input("Enter a number: "))
if is_palindrome(num):   
    print("This number is a palindrome number!")
else:  
    print("This number is not a palindrome number!")
