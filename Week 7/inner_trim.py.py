def tail(string):
    result = ""

    for i in range(1, len(string)):
        result += string[i]

    return result

def reverse(string):
    result = ""

    for ch in string:
        result = ch + result

    return result

def take(n, string):
    result = ""

    for i in range(0, n):
        result += string[i]

    return result

def drop(n, string):
    result = ""

    for i in range(n, len(string)):
        result += string[i]

    return result

def drop_start_spaces(string):
    counter = 0

    while string[counter] == " ":
        counter += 1

    return drop(counter, string)

def drop_end_spaces(string):
    string = reverse(string)

    return reverse(drop_start_spaces(string))

def inner_trim(string):
    result = ""

    string = drop_start_spaces(string)
#    string = drop_end_spaces(string)

    while True:
        while len(string) > 0 and string[0] != " ":
            result += string[0]

            string = tail(string)


        if len(string) == 0:
            break

        if len(string) > 1 and string[1] != " ":
            result += " "

        string = tail(string)

    return result
