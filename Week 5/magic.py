def sum_main_diagonal(matr):
    result = []

    for index in range (0, len(matr)):
        element = matr[index][index]
        result += [element]

    return sum(result)


def magic_square(square):
    main_diag = sum_main_diagonal(square)
    second_diag = sum_second_diagonal(square)
    if main_diag == second_diag :
        for index in range(0, len(sqaure)):
            if main_diag != sum_row(index,square)
            or
            main_diag != sum_col(index,square):
                return False

    return True
                

#glaven diagonal, vtorichen,redove,koloni
