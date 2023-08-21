import json
import random


class fileHandler:
    def find(self, id: int, findStr: str):
        ''' Функция поиска'''
        try:
            with open('data.txt') as json_file:
                data = json.load(json_file)
                for p in data['people']:
                    if int(id) == 1:
                        if p['firstName'] == findStr:
                            print('UID: ' + str(p['uid']))
                            print('Имя: ' + p['firstName'])
                            print('Фамилия: ' + p['lastName'])
                            print('Отчество: ' + p['fatherName'])
                            print('Организация: ' + p['orgName'])
                            print('Рабочий тел: ' + p['workPhone'])
                            print('Личный тел: ' + p['personalPhone'])
                            print('')
                    elif int(id) == 2:
                        if p['lastName'] == findStr:
                            print('UID: ' + str(p['uid']))
                            print('Имя: ' + p['firstName'])
                            print('Фамилия: ' + p['lastName'])
                            print('Отчество: ' + p['fatherName'])
                            print('Организация: ' + p['orgName'])
                            print('Рабочий тел: ' + p['workPhone'])
                            print('Личный тел: ' + p['personalPhone'])
                            print('')
                    elif int(id) == 3:
                        if p['fatherName'] == findStr:
                            print('UID: ' + str(p['uid']))
                            print('Имя: ' + p['firstName'])
                            print('Фамилия: ' + p['lastName'])
                            print('Отчество: ' + p['fatherName'])
                            print('Организация: ' + p['orgName'])
                            print('Рабочий тел: ' + p['workPhone'])
                            print('Личный тел: ' + p['personalPhone'])
                            print('')
                    elif int(id) == 4:
                        if p['orgName'] == findStr:
                            print('UID: ' + str(p['uid']))
                            print('Имя: ' + p['firstName'])
                            print('Фамилия: ' + p['lastName'])
                            print('Отчество: ' + p['fatherName'])
                            print('Организация: ' + p['orgName'])
                            print('Рабочий тел: ' + p['workPhone'])
                            print('Личный тел: ' + p['personalPhone'])
                            print('')
                    elif int(id) == 5:
                        if p['workPhone'] == findStr:
                            print('UID: ' + str(p['uid']))
                            print('Имя: ' + p['firstName'])
                            print('Фамилия: ' + p['lastName'])
                            print('Отчество: ' + p['fatherName'])
                            print('Организация: ' + p['orgName'])
                            print('Рабочий тел: ' + p['workPhone'])
                            print('Личный тел: ' + p['personalPhone'])
                            print('')
                    elif int(id) == 6:
                        if p['personalPhone'] == findStr:
                            print('UID: ' + str(p['uid']))
                            print('Имя: ' + p['firstName'])
                            print('Фамилия: ' + p['lastName'])
                            print('Отчество: ' + p['fatherName'])
                            print('Организация: ' + p['orgName'])
                            print('Рабочий тел: ' + p['workPhone'])
                            print('Личный тел: ' + p['personalPhone'])
                            print('')
        except Exception as e:
            print(e)


    def edit(self, id: int):
        ''' Функция редактирования по id '''
        try:
            with open('data.txt') as json_file:
                data = json.load(json_file)
                for i in range(len(data['people'])):
                    if data['people'][i]['uid'] == int(id):
                        print(data['people'][i])
                        del data['people'][i]
                        print('Введите новое Имя:')
                        firstName = input()
                        print('Введите новую Фамилию:')
                        lastName = input()
                        print('Введите новое Отчество:')
                        fatherName = input()
                        print('Введите новую Организацию:')
                        orgname = input()
                        print('Введите новый рабочий телефон:')
                        workPhone = input()
                        print('Введите новый личный телефон:')
                        personalPhone = input()
                        data['people'].append({
                            'uid': random.randrange(10000000, 100000000, 2),
                            'firstName': firstName,
                            'lastName': lastName,
                            'fatherName': fatherName,
                            'orgName': orgname,
                            'workPhone': workPhone,
                            'personalPhone': personalPhone
                        })
                        with open('data.txt', 'w') as outfile:
                            json.dump(data, outfile)
                            print('Данные изменены!')
                        break
        except Exception as e:
            print(e)


    def delete(self, id: id):
        ''' Функция удаления по id'''
        with open('data.txt') as json_file:
            try:
                data = json.load(json_file)
                for i in range(len(data['people'])):
                    if data['people'][i]['uid'] == int(id):
                        print(data['people'][i])
                        del data['people'][i]
                        with open('data.txt', 'w') as outfile:
                            json.dump(data, outfile)
                            print('Данные удалены!')
                        break
            except Exception as e:
                print(e)

    def list(self):
        ''' Функция вывода списка всего справочника построчно '''
        try:
            with open('data.txt') as json_file:
                data = json.load(json_file)
                for p in data['people']:
                    print('UID: ' + str(p['uid']))
                    print('Имя: ' + p['firstName'])
                    print('Фамилия: ' + p['lastName'])
                    print('Отчество: ' + p['fatherName'])
                    print('Организация: ' + p['orgName'])
                    print('Рабочий тел: ' + p['workPhone'])
                    print('Личный тел: ' + p['personalPhone'])
                    print('')
        except Exception as e:
            print(e)


    def add(self, firstName: str, lastName: str, fatherName: str, orgname: str, workPhone: str, personalPhone: str):
        ''' Функция добавления в справочник '''
        try:
            with open('data.txt') as json_file:
                    data = json.load(json_file)
                    data['people'].append({
                        'uid': random.randrange(10000000, 100000000, 2),
                        'firstName': firstName,
                        'lastName': lastName,
                        'fatherName': fatherName,
                        'orgName': orgname,
                        'workPhone': workPhone,
                        'personalPhone': personalPhone
                    })
        except FileNotFoundError:
            print('Нет файла, файл будет создан!')
            data = {}
            data['people'] = []
            data['people'].append({
                'uid': random.randrange(10000000, 100000000, 2),
                'firstName': firstName,
                'lastName': lastName,
                'fatherName': fatherName,
                'orgName': orgname,
                'workPhone': workPhone,
                'personalPhone': personalPhone
            })

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
