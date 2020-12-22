

user_seconds = int(input('Введите количество секунд: '))
hours = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = user_seconds % 60
print(f'{hours } часов {minutes} минут {seconds} секунд')


