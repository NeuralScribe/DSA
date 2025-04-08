str = input()
count_digits = 0
count_vowel =0
count_consonent = 0
for i in str:
    if "0" <= i and i <= "9":
        count_digits = count_digits+1
    else:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count_vowel = count_vowel+1
        else:
            count_consonent = count_consonent+1
print(count_digits)
print(count_vowel)
print(count_consonent)