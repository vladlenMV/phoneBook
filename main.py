from phonebook.fileHandler import fileHandler


while True:
    '''Стартовая справка'''
    print("Телефонный справочник")
    print("Введите команду: (commands - список команд)")
    print('')
    command = input()
    ''' Обработка команд '''
    if command == 'commands':
        print('Просмотр справочника - list')
        print('Добавить - add')
        print('Поиск - find')
        print('Редактирование - edit')
        print('Удаление - del')
        print('')
    elif command == 'list':
        fH = fileHandler()
        fH.list()
    elif command == 'find':
        fH = fileHandler()
        print("Поиск по Именни - 1")
        print("Поиск по Фамилии - 2")
        print("Поиск по Отчеству - 3")
        print("Поиск по Организации - 4")
        print("Поиск по Рабочему номеру - 5")
        print("Поиск по Личному номеру - 6")
        id = input()
        print("Введите слово для поиска")
        findStr = input()
        fH.find(id, findStr)
    elif command == 'add':
        fH = fileHandler()
        print('Введите Имя:')
        firstName = input()
        print('Введите Фамилию:')
        lastName = input()
        print('Введите Отчество:')
        fatherName = input()
        print('Введите Организацию:')
        orgname = input()
        print('Введите Рабочий телефон:')
        workPhone = input()
        print('Введите Личный телефон:')
        personalPhone = input()
        try:
            fH.add(firstName, lastName, fatherName, orgname, workPhone, personalPhone)
            print('Данные добавлены!')
        except Exception as e:
            print(e)
    elif command == 'edit':
        print('Введите id для редактирования')
        id = input()
        fH = fileHandler()
        fH.edit(id)
    elif command == 'del':
        print('Введите id для удаления')
        id = input()
        fH = fileHandler()
        fH.delete(id)

    else:
        print('Неверная команда!')