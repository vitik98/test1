bilets = int(input('Введите количество билетов:'))
total = 0

for ticket in range(bilets):
    age = int(input('Введите Ваш возраст:'))
    if age <= 18:
        total += 0
        print('Бесплатно')
    if 18 < age < 25:
        total += 990
        print('Cумма за билет:990')
    if age > 25:
        total += 1390
        print('Cумма за билет:1390')

if bilets >= 3:
    total = total * (100 - 10) / 100
print('Сумма за все выбранные билеты:', int(total))