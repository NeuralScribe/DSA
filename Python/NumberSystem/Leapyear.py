n = int(input("Enter the year: "))

if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("The provided year is Leapyear!")
else:
    print("The provided year is not leapyear!")