profit = float(input('Введите месячную выручку: '))
cost = float(input('Введите месячные издержки: '))

if profit > cost:
    print('Ваша фирма работает прибыльно')
elif profit < cost:
    print('Ваша фирма работает в убыток')
elif profit == cost:
    print('Ваша прибыль равна издержкам')

if profit > cost:
    rent_profit = profit / cost
    print(f'Рентабельность выручки составляет: {rent_profit}')

workers = int(input('Введите количество сотрудников: '))
worker_profit = profit / workers
print(f'Один сотрудник приносит фирме: {worker_profit} ')
