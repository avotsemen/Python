# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def replace_entry(lst):
    index_max_element = max(lst)
    index_min_element = min(lst)
    for i in range(0, len(lst)):
        if lst[i] == index_max_element:
            lst[i] = index_min_element
        elif lst[i] == index_min_element:
            lst[i] = index_max_element
    return lst

lst = [1, 3, 3, 3, 4]
print(replace_entry(lst))
