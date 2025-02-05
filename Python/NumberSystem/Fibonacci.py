num = int(input("Enter the number upto which u want to print the series:  "))
first_num = 0
second_num = 1
print(first_num)
print(second_num)
for i in range(0, num-2):
    sum = first_num + second_num
    print(sum)
    first_num = second_num
    second_num = sum