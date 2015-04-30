def is_decreasing(seq):
    n = len(seq)
    index = 0



    for index in range(0,n - 1):
        element = seq[index]
        neighbour = seq[index + 1]
        if element < neighbour:
            return False
        
        index += 1

    return True

print(is_decreasing([5,4,3,2,1]))