n = input("Enter n:")
n = int(n)

digits = []

while n != 0:
    digit = n % 10
    digits= [digit] + digits
    n = n // 10

print ("The list of digits" + str(digits))

n = 0

for digit in digits:
    n = n * 10 + digit

print("Number is " + str(n))
    
