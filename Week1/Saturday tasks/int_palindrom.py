n = input("Enter a number: ")
n = int(n)

non_reversed = n
reversed_number = 0

while n != 0:
    digit = n % 10

    reversed_number = reversed_number * 10 + digit

    n = n // 10

if non_reversed == reversed_number:
    print(str(non_reversed) + " is a palindrom")
else:
    print(str(non_reversed) + " is not a palindrom")
