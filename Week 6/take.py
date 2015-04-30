def take (x, numbers):
    index = 0
    end = x
    result = []


    for number in range(0,x):
        number = numbers[index]
        result += [number]
        
        index += 1
    return result

print(take(2, [1, 2, 3, 4, 5]))
print(take(3, [3, 4, 5, 6, 7, 8]))
print(take(1, [1]))