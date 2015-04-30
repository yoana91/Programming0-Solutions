def equal_lists(list_1, list_2):
    if len(list_1) != len(list_2):
        return False

    for index in range(0, len(list_1)):
        if list_1[index] != list_2[index]:
            return False

    

    return True
print (equal_lists([1, 2,3], [1, 3]))
    
