n = input("Enter n:")
n = int(n)

reversed_n = 0

while n!=0:
    digit = n%10
    reversed_n = reversed_n*10+digit
    n =n//10
print(reversed_n)
