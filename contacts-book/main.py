contacts = {}

while True:
    menu = '1:добавить\n 2:найти\n 3:показать все\n 4:удалить\n 0:выйти'
    print(menu)
    answ = input('Выберите что-то из меню: ')

    if answ == '0':
        print('Пока!')
        break
    elif answ == '1':
        namec = input('Введите имя: ')
        phonec = input('Введите номер: ')
        contacts[namec] = phonec
    elif answ == '2':
        search = input('Введите имя для поиска: ')
        if search in contacts:
            value = contacts.get(search)
            print(search, value)
        else:
            print('Контакт не найден')
    elif answ == '3':
        print(contacts)
    elif answ == '4':
        dell = input('Введите имя для удаления: ')
        if dell in contacts:
            del contacts[dell]
        else:
            print('Контакт не найден')


        

        


