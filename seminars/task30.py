# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

def ar_prog(a1, d, n):
    # Создаем пустой список для хранения элементов прогрессии
    progression = []
    
    # Заполняем список элементами арифметической прогрессии
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    
    return progression

def print_list(list):
    for i in list:
        print(i)

a1 = 2  # Первый элемент
d = 3   # Разность
n = 5   # Количество элементов

print_list(ar_prog(a1, d, n))