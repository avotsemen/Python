# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
# В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

def check_ritm(stroka):
    phrases = stroka.upper().split()
    if len(phrases) <= 1:
        return 'Количество фраз должно быть больше одной!'
    print(phrases)
    cnt_glas = lambda phrase: sum(1 for char in phrase if char in 'АЕЁИОУЫЭЮЯ')
    
    lst_cnt_glas = list(map(cnt_glas, phrases))
    if len(set(lst_cnt_glas)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'

stroka = 'пара-ра-рам рам-пам-Папам па-ра-па-дам'
check_ritm(stroka)
