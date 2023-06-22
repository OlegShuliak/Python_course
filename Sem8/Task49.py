

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

def modify_contact(name):
    temp = []
    with (open(file_path, 'r', encoding='utf-8')) as _data:
        for line in _data:
            temp.append(line)
    for line in temp:
         if name.lower() in line.lower():
            print(line.replace(';', ' ').replace('\n', ''))
            mod_fio = input('Измените ФИО через пробел: ')
            mod_number = input('Измените номер: ')
            temp.remove(line)
            temp.append(f'{mod_fio} {mod_number}\n'.replace(' ', ';'))
    with (open(file_path, 'w', encoding='utf-8')) as _data:
        for line in temp:
            _data.write(line)
        
def delete_contact(name):
    temp = []
    with (open(file_path, 'r', encoding='utf-8')) as _data:
        for line in _data:
            temp.append(line)
    for line in temp:
         if name.lower() in line.lower():
            print(line.replace(';', ' ').replace('\n', ''))
            print('Контакт удален')
            temp.remove(line)
    with (open(file_path, 'w', encoding='utf-8')) as _data:
        for line in temp:
            _data.write(line)

def main():
    print('Выберите действие:', '\n',
          '1 - Показать справочник', '\n',
          '2 - Найти контакт', '\n',
          '3 - Добавить контакт', '\n',
          '4 - Изменить контакт', '\n',
          '5 - Удалить контакт')
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
    elif select == 4:
        mod_name = input('Введите фамилию контакта, который хотите изменить: ')
        modify_contact(mod_name)
    elif select == 5:
        del_name = input('Введите фамилию контакта, который хотите удалить: ')
        delete_contact(del_name)

main()






