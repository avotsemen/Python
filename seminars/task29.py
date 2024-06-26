'''
Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)
'''
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)

# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)
# 

n = int(input('Введите неотрицательное число: '))
max_number = 0
while n != 0:
    n = int(input('Введите неотрицательное число: '))
    if max_number < n:
        max_number = n
print(max_number)