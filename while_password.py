message = ''
password = []
while message != 'secret':
    message = input('Введите пароль: ')
    password.append(message)
    if message == 'secret':
        print('Коректный пароль')
        break
    print('не правильный пассворд')
    print(password)
    print