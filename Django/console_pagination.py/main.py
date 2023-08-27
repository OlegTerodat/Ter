import csv

FILE_NAME = "phonebook.csv"
FIELDS = ["Фамилия", "Имя", "Отчество", "Организация", "Телефон рабочий", "Телефон личный"]

def load_data():
    """Загрузка данных из CSV-файла."""
    data = []
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    """Сохранение данных в CSV-файл."""
    with open(FILE_NAME, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)

def add_entry():
    """Добавление новой записи в справочник."""
    entry = {}
    for field in FIELDS:
        entry[field] = input(f"Введите {field.lower()}: ")
    return entry

def search_entries(search_field, search_value, data):
    """Поиск записей по заданной характеристике."""
    return [entry for entry in data if entry[search_field].lower() == search_value.lower()]

def edit_entry(data):
    """Редактирование записи."""
    print("\nДоступные записи:")
    for idx, entry in enumerate(data):
        print(f"{idx}: {entry}")

    entry_id = int(input("\nВведите номер записи для редактирования: "))
    if 0 <= entry_id < len(data):
        entry = data[entry_id]
        for field in FIELDS:
            new_value = input(f"Текущее значение {field}: {entry[field]}. Введите новое значение или оставьте пустым для сохранения текущего: ")
            if new_value:
                entry[field] = new_value
        print("Запись успешно обновлена.")
    else:
        print("Неверный номер записи.")

def delete_entry(data):
    """Удаление записи."""
    print("\nДоступные записи:")
    for idx, entry in enumerate(data):
        print(f"{idx}: {entry}")

    entry_id = int(input("\nВведите номер записи для удаления: "))
    if 0 <= entry_id < len(data):
        deleted = data.pop(entry_id)
        print(f"Запись {deleted} успешно удалена.")
    else:
        print("Неверный номер записи.")

def main():
    data = load_data()

    while True:
        choice = input("\nВыберите действие:\n1. Добавить запись\n2. Поиск\n3. Показать все\n4. Редактировать запись\n5. Удалить запись\n6. Выход\n")

        if choice == "1":
            data.append(add_entry())
            save_data(data)
        elif choice == "2":
            search_field = input("По какому полю: Имя, Фамилия, и т.д ")
            search_value = input("Введите значение для поиска: ")
            results = search_entries(search_field, search_value, data)
            for result in results:
                print(result)
        elif choice == "3":
            for entry in data:
                print(entry)
        elif choice == "4":
            edit_entry(data)
            save_data(data)
        elif choice == "5":
            delete_entry(data)
            save_data(data)
        elif choice == "6":
            break

if __name__ == "__main__":
    main()
