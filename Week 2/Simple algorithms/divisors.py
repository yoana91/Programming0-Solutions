n = input("Enter n:")
n = int(n)

start = 1
end = n - 1
divisors = []

while start <= end:
    if n % start == 0:
       divisors = divisors + [start]

    start += 1


print(divisors)
