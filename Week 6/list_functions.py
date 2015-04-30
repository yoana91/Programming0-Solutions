def head(lists):
    return lists[0]

a = [1,2,3]
print(head(a))

b = ["Python"]
print(head(b))

def last(lists):
    return  lists[ len(lists) - 1]


c = [1,2,3]
print(last(c))

d = ["Python"]
print(head(d))


def tail(lists):
    index = 1
    n = len(lists) 
    result = []

    for index in range(1,n):
        element = lists[index]
        result += [element]

        



    return result

f = [1,2,3]
print(tail(f))

e = ["Python"]
print (tail(e))


def equal_lists(list_1, list_2):
    if len(list_1) != len(list_2):
        return False

    while len(list_1) != 0:
        if head(list_1) != head(list_2):
            return False
        list_1 = tail(list_1)
        list_2 = tail(list_2)

    return True
print (equal_lists([1, 2,3], [1, 3]))


print (equal_lists([1, 2,3], [1, 3]))
print(equal_lists([], []))

def count_item(x, numbers):
    counter = 0
    
    for number in numbers:
        if x == number:
            counter += 1


    return counter


print(count_item(5, [1, 2, 3, 4, 5]))

print(count_item("winter", ["winter", "winter"]))

print(count_item(False, [True, True]))


def take (n, items):
    
    result = []
    if n > len(items):
        n = len(items)


    for index in range(0,n):
        result += [items[index]]
        
        
        
    return result

print(take(2, [1, 2, 3, 4, 5]))
print(take(3, [3, 4, 5, 6, 7, 8]))
print(take(10, [1]))

def take_2(n, items):
    result = []
    taken = 0

    while taken != n and len(items) != 0:
        item = head(items)
        result += [item]
        taken += 1
        items = tail(items)

    return result



def drop(x, numbers): 
    n = len(numbers)
    result = []
    index = x

    for index in range(x, n):
        number = numbers[index]
        result += [number]

        
    return result


print (drop(1, [1, 2, 3]))
print(drop(2, ["Python", "Ruby", "Django", "Rails"]))
print(drop(10, [1]))

def reverse(items):
    result = []
    for item in items:
        result = [item] + result
    
    return result

print(reverse([1, 2, 3])))

def reverse_2 (items):
    result = []
    last_index = len(items) - 1
    while last_index >= 0 :
        result += [items[last_index]]
        last_index -= 1

    return result




    
        
        


























            




















    
