def check_amount(n):
    if not n.isdigit():
        return False
    if int(n) < 2:
        return False
    return int(n)


def check_names(n, str1, str2):
    names = []
    for i in range(n):
        print(f'Введите название {str1} {i + 1}')
        name = input()
        while name in names or name == '':
            print(f'Такой {str2} уже существует или введена пустая строка. Введите другое название {str1} {i + 1}')
            name = input()
        names.append(name)
    return names


def fill_matrix(n, names, str1, str2):
    matrix = [[1.0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        for j in range(1, n - i):
            print(f'Сравните {str1} "{names[i]}" и {str1} "{names[i + j]}" {str2}')
            k = input()
            while k.isalpha():
                print(f'Введите целое или дробное число. Сравните {str1} "{names[i]}" и {str1} "{names[i + j]}"')
                k = input()
            matrix[i + j][i] = float(k)
            matrix[i][i + j] = 1 / float(k)
    return matrix


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(round(j, 2), end=f'{" " * (5 - len(str(round(j, 2))))}')
        print()


def oksv_and_novp(matrix):
    oksv = []
    for i in matrix:
        n = 1
        for j in i:
            n *= j
        oksv.append(n ** 0.2)
    novp = [i / sum(oksv) for i in oksv]
    print(f'''Оценки компонента собственного вектора: {[round(i, 2) for i in oksv]}
Нормализованные оценки вектора приоритета {[round(i, 4) for i in novp]}\n''')
    return novp


if __name__ == '__main__':
    print('Введите количество критериев (больше одного)')
    amount_of_kr = check_amount(input())
    while not amount_of_kr:
        print('Введено не допустимое значение. Ведите количество критериев (больше одного)')
        amount_of_kr = check_amount(input())

    print('Введите количество объектов для сравнения')
    amount_of_obj = check_amount(input())
    while not amount_of_obj:
        print('Введено не допустимое значение. Ведите количество критериев (больше одного)')
        amount_of_obj = check_amount(input())

    names_kr = check_names(amount_of_kr, 'критерия', 'критерий')
    matrix_kr = fill_matrix(amount_of_kr, names_kr, 'критерий', '')

    print_matrix(matrix_kr)
    novp_kr = oksv_and_novp(matrix_kr)

    names_obj = check_names(amount_of_obj, 'объекта', 'объект')
    all_novp = []

    for i in range(amount_of_kr):
        matrix_obj = fill_matrix(amount_of_obj, names_obj, 'объект', f'по критерию "{names_kr[i]}"')
        print_matrix(matrix_obj)
        novp_obj = oksv_and_novp(matrix_obj)
        all_novp.append(novp_obj)

    results = {}
    for i in range(amount_of_obj):
        n = 0
        for j in range(amount_of_kr):
            print(round(all_novp[j][i], 3), end=' ')
            n += all_novp[j][i] * novp_kr[j]
        print(round(n, 3))
        results[f'{names_obj[i]}'] = n
    print()
    result = sorted(results, key=results.get)[::-1]
    for i in result:
        print(f'{i} - {round(results[i], 3)}')
    print()
