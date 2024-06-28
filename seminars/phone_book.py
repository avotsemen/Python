# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Файл для хранения данных

filename = 'phone.txt'

def main():
    phonebook = read_txt(filename)
    while True:
        choice = show_menu()
        if choice == 1:
            print(print_phonebook(phonebook))
        elif choice == 2:
            search_user(phonebook)
        elif choice == 3:
            add_user(phonebook)
        elif choice == 4:
            write_txt(filename, phonebook)
        elif choice == 5:
            print('Сохранить телефонный справочник?\n'
                  '     1 - Да  |   0 - Нет')
            if int(input()) != 0:
                write_txt(filename , phonebook)
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def show_menu():
    print("     Телефонный справочник: \n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента \n"
          "3. Добавить абонента в справочник\n"
          "4. Сохранить справочник в текстовом формате\n"
          "5. Закончить работу")
    choice = int(input("Выберите необходимое действие: "))
    return choice

def read_txt(filename): 

    phonebook=[]

    fields= ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
           record = dict(zip(fields, line.split(',')))
           phonebook.append(record)
           	
    return phonebook

def print_phonebook(phonebook): # 1
    print("Список абонентов:")
    print()
    for record in phonebook:
        print(*record.values(), end = '', sep = ' | ')
    print()

def search_user(phonebook): # 2
    print("Поиск абонента в справочнике")
    print()
    search = input("Введите имя или фамилию абонента: ")
    for record in phonebook:
        if search in record.values():
            print(*record.values(), end = '', sep = ' | ')
    print()

def add_user(phonebook): # 3
    print("Добавление абонента в справочник")
    print()
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = {}
    for field in fields:
        record[field] = input(f'Введите {field}: ')
    if field != 'Описание':
        phonebook.append(record)
    else:
        record['Описание'] += '\n'
        phonebook.append(record)
    print(phonebook)
    print()

def write_txt(filename , phonebook):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phonebook)):

            s=''
            for v in phonebook[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}')
    
    print('\n'
          f'Справочник сохранен в файл "{filename}"'
          '\n'
          )  

main()
