goods = []
featuers = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: '). upper() == 'Q' :
        break
    num += 1
    for f in featuers.keys():
        user_data = input(f'{f}: ')
        featuers[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(featuers[f])
    goods.append((num, featuers.copy()))
    print('Текущая аналитика по товарам: \n')
    for key, value in analitics.items():
        print(key, value)