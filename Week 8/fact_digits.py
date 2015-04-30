def factorial(n):
    result = 1
    start = 1

    while start <= n:
        result *= start
        start += 1

    return result

def to_digits(n):
    result = []
    
    while n != 0:
        digit = n % 10
        
        result = [digit] + result

        n = n // 10

    return result

def fact_digits(n):
	digits = to_digits(n)
	sum = 0

	for digit in digits:

		sum += factorial(digit)

	return sum

n = input("Enter:")
n = int(n)

print(fact_digits(n))