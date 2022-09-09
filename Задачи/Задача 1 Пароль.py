while True:
    password1 = input('Введите пароль ')
    password2 = input('Повторите пароль ')
    a = True
    if len(password1) <8:
        a = False
        print('Короткий!')
    if '123' in password1:
        a = False
        print('Простой!')
    if password1 != password2:
        a = False
        print('Различаются')
    if a:
        break
print('Пароли совпадают!')