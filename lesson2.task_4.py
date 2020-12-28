user_answ = input('Введите несколько слов через пробел: ')

for i, word in enumerate(user_answ.split(), 1):
    print(i, word[:10])