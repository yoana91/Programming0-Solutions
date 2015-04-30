n = input("Enter n:")
n = int(n)

start = 1
divisors = []
end = n - 1
sum = 0

while start <= end:
    if  n % start == 0:
        divisors = divisors + [start]

    start += 1

print(divisors)

for divisor in divisors:
    sum = sum + divisor

print("The sum of divisors is "+ str(sum))
    
