string = input("Enter string:")

counter = 0

vowels = "aeiouyAEIOUY"

for ch in string:
    if ch in vowels:
        counter += 1

print("The number of vowels is " + str(counter))
