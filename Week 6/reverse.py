def reverse(items):
    result = []
    for item in items:
        result = [item] + result
    
    return result

 print(reverse([1, 2, 3]))