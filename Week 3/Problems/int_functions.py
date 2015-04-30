def reverse_int(n):
    digits = []
    while n!= 0:
        digit = n % 10
        digits = digits + [digit]
        n = n // 10

    return digits
    
def sum_digits(x):
    digit_sum = 0

    while x != 0:
        digit = x % 10
        
        digit_sum += digit

        x = x // 10

    return digit_sum

def product_digits(n):
    product = 1
    

    while n != 0:
        digit = n % 10
        product = product * digit
        n = n // 10 

    return product 

a = input("Enter a :")
a = int(a)

reverse_a = reverse_int(a)
print(reverse_a)

sum_digits_a = sum_digits(a)
print(sum_digits_a)

product_digits_a = product_digits(a)
print(product_digits_a)


