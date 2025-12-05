# Исходные данные
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}



# Функция для поиска владельца документа по номеру
def find_document_owner(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return None


# Основная логика программы с циклом ввода команд
def main():
    while True:
        command = input('Введите команду: ')

        if command == 'q':  # Завершение программы
            print('Программа завершена.')
            break

        elif command == 'p':  # Команда для поиска владельца документа
            doc_number = input('Введите номер документа: ')
            owner = find_document_owner(doc_number)
            if owner:
                print(f'Владелец документа: {owner}')
            else:
                print('Документ не найден в базе')

        else:
            print('Неизвестная команда. Используйте "p" для поиска владельца или "q" для выхода.')


# Запуск программы
if __name__ == '__main__':
    main()
