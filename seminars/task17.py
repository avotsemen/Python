# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

def count_different(lst):
    return len(set(lst))

lst = [1, 1, 2, 0, -1, 3, 4, 4]
print(count_different(lst))