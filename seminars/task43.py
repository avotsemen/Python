# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:       Вывод:
# 1 2 3 2 3   2

def create_array(n):
    lst = []
    for i in range(n):
        lst.append(int(input('Введите элемент массива: ')))
    return lst

def count_pairs(lst):
    counts = {}
    pairs = 0

    # Подсчет количества вхождений каждого числа в списке
    for number in lst:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    # Подсчет пар
    for count in counts.values():
        pairs += count // 2

    return pairs

n = int(input('Введите количество элементов массива: '))
lst = create_array(n)
print(count_pairs(lst))

