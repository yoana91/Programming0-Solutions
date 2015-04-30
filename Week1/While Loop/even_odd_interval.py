a = input("Enter a:")
a = int(a)
b = input("Enter b:")
b = int (b)

start = a
end = b

while start <= end:
    print(start)
    if start%2==0:
        print(str(start)+" is even")
    elif start%2!=0:
        print (str(start)+"is odd")
    start = start+1
    
