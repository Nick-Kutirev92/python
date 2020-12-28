#Решение через list
seasons = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
user_answ = int(input('Введите номер месяца: '))

if user_answ in seasons[0:3]:
    print('Месяц относится ко времени года зима')
elif user_answ in seasons[3:6]:
    print('Месяц относится ко времени года весна')
elif user_answ in seasons[6:9]:
    print('Месяц относится ко времени года лето')
elif user_answ in seasons[9:12]:
    print('Месяц относится ко времени года осень')
else:
    print('Введите число от 1 до 12')








