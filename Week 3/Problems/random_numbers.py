from random import randint

def generate_random_list(n, start, end):

    counter = 1

    random_numbers = []

    while counter <= n:
        random_number = randint(start, end)
        random_numbers += [random_number]

        counter += 1

    return random_numbers

n_1 = input("Enter n_1:")
n_1 = int(n_1)


start_1 = input("Enter start_1 :")
start_1 = int(start_1)

end_1 = input("Enter end_1:")
end_1 = int(end_1)

generate_random_list_1 = generate_random_list(n_1,start_1,end_1)
print(generate_random_list_1)
