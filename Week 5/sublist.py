def sublist(list_1, list_2):

    result = []

    for item in list_2:

        index_list_1 = 0
        
        while index_list_1 < len(list_1):
            if list_1[index_list_1] == item:
                result += [list_1[index_list_1]]
                
            index_list_1 += 1



    if result == list_1:
        print(str(list_1) + " is sublist of " + str(list_2))
        return True

    return False

a = ["Python", "Django"] 
b = ["Django", "Python"]
print(sublist(a, b))
