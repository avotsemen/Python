# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input('Введите количество арбузов: '))
arbuz = []
for i in range(n):
    arbuz.append(int(input('Введите массу арбуза: ')))
ma = arbuz[0]
mi = arbuz[0]
for i in arbuz:
    if i > ma:
        ma = i
    if i < mi:
        mi = i
        
print(f'Самый легкий арбуз весит {mi} кг')
print(f'Самый тяжелый арбуз весит {ma} кг')