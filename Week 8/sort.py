def min_element(numbers):

    min_index = 0
    index = 0
    
    
    for number in numbers:
        if number < numbers[min_index]:
            min_index = index

        index += 1


    return min_index

def basic_sort(numbers):
    new_list = []

    while True:
        new_list += [numbers[min_element(numbers)]]

        del numbers[min_element(numbers)]

        if len(numbers) == 0:
            break

    return new_list

print(basic_sort([2, 1, 5, 4]))













