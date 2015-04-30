def to_matrix(n, list):
    result = []
    while True:
        for string in list:
            characters = []

            i = 0

            while i < n:
                if i >= len(string):
                    characters += ["X"]
                else:
                    characters += [string[i]]

                i += 1

            result += [characters]

        m = n

        if m > len(list):
            while m - len(list) > 0:
                result += [["X"] * n]
                m -= 1

        if len(result) == n:
            break

    return result

def string_matrix(matrix):
    result = ""

    for row in matrix:
        for element in row:
            result += "| " + element + " "

        result += "|" + "\n"

    return result
