from phone_book import (load_contacts,
                        save_contacts,
                        find_contacts,
                        input_search_criteria,
                        print_contacts
                        )

FILE_PATH = 'contacts.txt'
def main():
    contacts = load_contacts(FILE_PATH)
    while True:
        print(
            '1 - Вывод всех контактов\n'
            '2 - Поиск контактов\n'
            '3 - Сохранение\n'
            '4 - Выход\n'
            )
        option = input('Выберите пункт: ')
        if option == '1':
            print_contacts(contacts)
        if option == '2':
            criteria = input_search_criteria()
            found = find_contacts(contacts, **criteria)
            print_contacts(found)
        if option == '3':
            save_contacts(FILE_PATH, contacts)
        if option == '4':
            break


if __name__ == "__main__":
    main()
