n = input("Enter n:")
n = int(n)
start=1
sum = 0
while start<=n:
    
           
    if start%2 == 0:
        sum = sum+start

        print(str(start) + "is even")
    start= start+1
print("The sum is" +" " + str(sum))
