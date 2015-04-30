def setify(a):
    result = []

    for element in a:
        if element not in result:
            result.append(element)

    return result




def diff(a, b):
    result = []

    for item in setify(a):
        if item not in setify(b):
            result.append(item)

    return result




def union(a, b):
    result = []

    result = setify(a) + setify(b)
    result = setify(result)
    return result




def intersection(a, b):
    result = []

    for element in a:
        if element in b:
            result.append(element)

    result = setify(result)

    return result



def cartesian_product(a, b):
    result = []

    for i in setify(a):
        for j in setify(b):
            result.append((i, j))

    return result
