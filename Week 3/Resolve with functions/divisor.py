def divisor(n):
    
    start = 1
    end = n - 1 
    divisors = []
 
    while start <= end:
        if n % start == 0:
           divisors = divisors + [start]
 
        start += 1
    return divisors


a = input("Enter a:")
a = int(a)


divisors_a = divisor(a)
print(divisors_a)
