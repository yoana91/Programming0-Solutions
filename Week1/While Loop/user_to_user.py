start = input("Enter start: ")
start = int(start)

end = input("Enter end: ")
end = int(end)


counter = start

print("Counting from " + str(counter) +  " to " + str(end))

while counter <= end:
    print(counter)

    
    counter = counter + 1


print("Counting from " + str(end) +" to " + str(start))

while end >= start:
    print(end)

    end = end - 1
