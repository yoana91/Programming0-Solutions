n = input("Enter n:")
n = int(n)
sum = 0 
while n !=0:
    digit = n%10

    sum = sum + digit
    n = n//10

print("The sum is" + " " + str(sum))
    
    
    
