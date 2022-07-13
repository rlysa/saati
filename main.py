print('Введите количество критериев')
amount_of_kr = int(input())

matrix_kr = [['_' for _ in range(amount_of_kr)] for _ in range(amount_of_kr)]
for i in range(amount_of_kr):
    matrix_kr[i][i] = 1.0

print('Введите названия критериев через запятую')
names_kr = input().split(', ')  # цена, размер, внешний вид

for i in range(amount_of_kr - 1):
    for j in range(1, amount_of_kr - i):
        print(f'Сопоставьте критерий "{names_kr[i]}" и критерий "{names_kr[i + j]}"')
        k = float(input())
        matrix_kr[i + j][i] = k
        matrix_kr[i][i + j] = 1 / k

oksv_kr = []
for i in matrix_kr:
    n = 1
    for j in i:
        n *= j
    oksv_kr.append(n ** 0.2)
novp_kr = [i / sum(oksv_kr) for i in oksv_kr]


print()
for i in matrix_kr:
    for j in i:
        print(round(j, 2), end=f'{" " * (5 - len(str(round(j, 2))))}')
    print('')
print(f'''Оценки компонента собственного вектора: {[round(i, 2) for i in oksv_kr]}
Нормализованные оценки вектора приоритета {[round(i, 4) for i in novp_kr]}''')
print()

print('Введите количество объектов для сравнения')
amount_of_obj = int(input())

print('Введите названия сравниваемых объектов через запятую')
names_obj = input().split(', ')  # цена, размер, внешний вид

all_novp = []

for m in range(amount_of_kr):
    matrix_obj = [['_' for _ in range(amount_of_obj)] for _ in range(amount_of_obj)]
    for i in range(amount_of_obj):
        matrix_obj[i][i] = 1.0

    for i in range(amount_of_obj - 1):
        for j in range(1, amount_of_obj - i):
            print(f'Сопоставьте объект "{names_obj[i]}" и объект "{names_obj[i + j]}" по критерию "{names_kr[m]}"')
            k = float(input())
            matrix_obj[i + j][i] = k
            matrix_obj[i][i + j] = 1 / k

    oksv_obj = []
    for i in matrix_obj:
        n = 1
        for j in i:
            n *= j
        oksv_obj.append(n ** 0.2)
    novp_obj = [i / sum(oksv_obj) for i in oksv_obj]
    all_novp.append(novp_obj)

    print()
    for i in matrix_obj:
        for j in i:
            print(round(j, 2), end=f'{" " * (5 - len(str(round(j, 2))))}')
        print('')
    print(f'''Оценки компонента собственного вектора: {[round(i, 2) for i in oksv_obj]}
Нормализованные оценки вектора приоритета {[round(i, 4) for i in novp_obj]}''')
    print()

results = {}
for i in range(amount_of_obj):
    n = 0
    for j in range(amount_of_kr):
        print(round(all_novp[j][i], 7), end=' ')
        n += all_novp[j][i] * novp_kr[j]
    print(round(n, 9))
    results[f'{names_obj[i]}'] = n
print()
result = sorted(results, key=results.get)[::-1]
for i in result:
    print(f'{i} - {round(results[i], 9)}')
print()
