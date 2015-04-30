N = input("Enter N:")
M = input("Enter M:")
M = int(M)
N = int(N)
lower_bound = 0
upper_bound = 0
if N<M:
    lower_bound = N
    upper_bound = M
else:
    lower_bound = M
    upper_bound =N
    
start = lower_bound



while start<=upper_bound:
    sum = 0
    n = start
    while n!=0:
        digit = n%10
        sum = sum+digit
        n = n//10
    print(sum)
    start = start+1

#print(start_digit_sum)
#print(digit)


