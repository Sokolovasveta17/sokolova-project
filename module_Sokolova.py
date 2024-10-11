def print_org_names_and_phones(element):
    # Поиск массивов и элементов
    for array_element in element.findall('array'):
        for item_element in array_element.findall('item'):
            # Извлечение названия организации
            org_name = item_element.find('Name').text.strip() if item_element.find('Name') is not None else 'N/A'
            # Извлечение номера телефона
            phone_number = item_element.find('PublicPhone/PublicPhone').text.strip() if item_element.find('PublicPhone/PublicPhone') is not None else 'N/A'
            # Форматирование телефонного номера
            if phone_number != 'N/A':
                phone_number = '8' + phone_number
            # Вывод имени и номера телефона
            print(f"{org_name} {phone_number}")     
# Вывод названия организации и номера телефона
print_org_names_and_phones(root_element)


def print_names_and_phones(search_term):
    # Ищем название, которое содержит search_term (например, "школа")
    for array_element in root_element.findall('array'):
        for item_element in array_element.findall('item'):
            name = item_element.find('Name').text if item_element.find('Name') is not None else 'N/A'
            phone_number = item_element.find('PublicPhone/PublicPhone').text if item_element.find('PublicPhone/PublicPhone') is not None else 'N/A'            
            # Если название содержит искомое слово, выводим его
            if search_term.lower() in name.lower():
                if phone_number != 'N/A':
                    phone_number = '8' + phone_number
                print(name, phone_number)
# Запрашиваем ввод у пользователя
search_term = input("Введите слово(а) для поиска (например, 'поликлиника'): ")
print_names_and_phones(search_term)


def print_names_and_emails(search_term):
    # Ищем название, которое содержит search_term (например, "школа")
    for array_element in root_element.findall('array'):
        for item_element in array_element.findall('item'):
            name = item_element.find('Name').text if item_element.find('Name') is not None else 'N/A'
            email = item_element.find('Email/Email').text if item_element.find('Email/Email') is not None else 'N/A'            
            # Если название содержит искомое слово, выводим его
            if search_term.lower() in name.lower():
                print(name, email)
# Запрашиваем ввод у пользователя
search_term = input("Введите слово(а) для поиска (например, 'школа'): ")
print_names_and_emails(search_term)


def extract_names_and_emails(root_element):
    data = []
    for array_element in root_element.findall('array'):
        for item_element in array_element.findall('item'):
            name = item_element.find('Name').text
            email = item_element.find('Email/Email').text
            data.append((name, email))
    return data
search_term = input("Введите слово(а) для поиска (например, 'учреждение культуры'): ")
names_and_emails = extract_names_and_emails(root_element)
# Ищем email по названию
for name, email in names_and_emails:
    if search_term.lower() in name.lower():
        print(email)




