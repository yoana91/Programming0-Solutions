def is_increasing(seq):
    n = len(seq)
    index = 0



    for index in range(0,n - 1):
        element = seq[index]
        neighbour = seq[index + 1]
        if element > neighbour:
            return False
        
        index += 1

    return True

print(is_increasing([1,2,3,4,5]))
print(is_increasing([5,6,-10]))
print(is_increasing([1,1,1,1]))
print(is_increasing([1]))



