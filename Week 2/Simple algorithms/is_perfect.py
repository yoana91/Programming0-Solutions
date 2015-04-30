n = input("Enter n:")
n = int(n)

start = 1
end = n - 1

divisors = []

while start <= end:
    if n % start == 0:
        divisors = divisors + [start]

    start += 1



sum = 0

for divisor in divisors:
    sum = sum + divisor


print ("The sum is " + str(sum))

if sum == n:
    print("The number is perfect")
else:
    print("The number is not perfect")
