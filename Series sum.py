# 1 + 2 + 3 + 4 + 5 + .... + n

n = int(input("Enter the last number : "))

sum = 0
for i in range(1,n+1,1):
    sum = sum + i
print(sum)

a = int(input("Enter the last number: "))
sum = 0
for i in range(1, n+1, 1):
    sum = sum + i*i
print(sum)