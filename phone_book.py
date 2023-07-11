def load_contacts(file_path: str) -> list[dict[str, str]]: #аннотация типов, какой тип данных возвращает функция
    # contacts_file = open(file_path, 'r', encoding='utf-8')
    # ...
    # contacts_file.close()

    contacts = list()
    with open(file_path, 'r', encoding='utf-8') as contacts_file:
        for line in contacts_file:
            firstname, patronymic, lastname, phone = line.strip().split('#')
            contacts.append({
                'firstname': firstname,
                'patronymic': patronymic,
                'lastname': lastname,
                'phone': phone,
            })
    return contacts


def save_contacts(file_path: str, contacts: list[dict[str, str]]) -> None: #Если функция ничего не возвращает, вернется None
    with open(file_path, 'w', encoding='utf-8') as contacts_file:
        for contact in contacts:
            contact_str = '#'.join((
                contact['firstname'],
                contact['patronymic'],
                contact['lastname'],
                contact['phone'],
            ))
            print(contact_str, file=contacts_file)


def find_contacts(
    contacts: list[dict[str, str]], #где ищем
    firstname: str | None = None, #что ищем
    patronymic: str | None = None,
    lastname: str | None = None,
    phone: str | None = None,# Тип данных - строка или None
) -> list[dict]:
    found: list[dict[str, str]] = list()
    for contact in contacts:
        if (
            (firstname is None or contact['firstname'].lower() == firstname) and
            (patronymic is None or contact['patronymic'].lower() == patronymic) and
            (lastname is None or contact['lastname'].lower() == lastname) and
            (phone is None or contact['phone'].lower() == phone)
        ):
            found.append(contact)
    return found
            


def input_search_criteria() -> dict[str, str]:
    print(
        '1 - поиск по имени\n'
        '2 - поиск по отчеству\n'
        '3 - поиск по фамилии\n'
        '4 - поиск по номеру телефона'
    )
    user_choice = int(input('Укажите по какому критерию искать: '))
    if user_choice == 1:
        firstname = (input('Введите имя: ')).lower()
        return {'firstname': firstname}
    if user_choice == 2:
        patronymic = input('Введите фамилию: ').lower() 
        return {'patronymic': patronymic}
    if user_choice == 3:
        lastname = input('Введите фамилию: ').lower()
        return {'lastname': lastname}
    if user_choice == 4:
        phone = input('Введите номер телефона').lower()
        return {'phone': phone}
    return dict()

def print_contacts(contacts: list[dict[str, str]]):
    for contact in contacts:
        print(' '.join((
            contact["lastname"],
            contact["firstname"],
            contact["patronymic"],
            f'({contact["phone"]})',
        )))



# contacts = [
#     {'name': 'a'},
#     {'name': 'b'}
# ]

# x = contacts[0]
# x['name'] = 'c'

# print(contacts[0])

# contacts = load_contacts('contacts.txt')
# criteria = input_search_criteria()
# found_contacts = find_contacts(contacts, **criteria)
# save_contacts('contacts.txt', contacts)