message = ''

while message != 'secret':
    message = input('Введите пароль: ')
    if message == 'secret':
        print('Коректный пароль')
        break
    print('не правильный пассворд')
    