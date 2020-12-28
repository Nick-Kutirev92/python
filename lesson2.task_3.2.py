seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
user_answ = int(input('Введите номер месяца: '))
for key in seasons:
    if user_answ in seasons[key]:
        print('Месяц относится ко времен года ' + key)
