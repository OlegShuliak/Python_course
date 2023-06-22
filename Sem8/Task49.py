# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

file_path = 'D:\\GeekBrains\\Python_course\\Sem8\\Spravochnik.txt'

def show_all_records():
    with (open(file_path, 'r', encoding='utf-8')) as _data:
        for line in _data:
            phonebook_data = line.replace(';', ' ') 
            print(phonebook_data, end='')

def search_record(name):
     with (open(file_path, 'r', encoding='utf-8')) as _data:
        for line in _data:
            if name.lower() in line.lower():
                print(line.replace(';', ' '))
                return
        print(f'Контакта {name} не существует.')

def add_contact(fio, number):
    with open(file_path, 'a', encoding='utf-8') as _data:
        _data.write('\n')
        _data.write(fio.replace(' ', ';'))
        _data.write(';')
        _data.write(number)

def main():
    print('Выберите действие:',
          '1 - Показать справочник',
          '2 - Найти контакт',
          '3 - Добавить контакт')
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        second_name = input('Введите фамилию: ')
        search_record(second_name)
    elif select == 3:
        new_contact_fio = input('Введите ФИО через пробел: ')
        new_contact_number = input('Введите номер: ')
        add_contact(new_contact_fio, new_contact_number)

main()






