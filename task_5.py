profit = float(input('Введите месячную выручку: '))
costs = float(input('Введите месячные издержки: '))

result = profit - costs
if result > costs:
    print('Ваша фирма работает прибыльно, ваша выручка состовляет', result)
elif result < costs:
    print('Ваша фирма работает в убыток')
elif result == costs:
    print('Ваша прибыль равна издержкам')

if profit > costs:
    rent_profit = profit / costs
    print(f'Рентабельность выручки составляет: {rent_profit}')



workers = int(input('Введите количество сотрудников: '))
worker_profit = result / workers
print(f'Один сотрудник приносит фирме: {worker_profit} ')