
sweets = ["шоколад", "мармелад", "леденцы", "печенье", "торт"]


def show_sweets():
    print("\nСписок сладостей:")
    if not sweets:
        print("Список пуст.")
        return

    for number, sweet in enumerate(sweets, start=1):
        print(f"{number}. {sweet}")


def add_sweet():
    new_sweet = input("\nВведите название сладости: ").strip().lower()

    if not new_sweet:
        print("Название не должно быть пустым.")
        return

    sweets.append(new_sweet)
    print("Сладость добавлена.")


def find_sweet():
    query = input("\nВведите название для поиска: ").strip().lower()

    if not query:
        print("Введите текст для поиска.")
        return

    found_items = [sweet for sweet in sweets if query in sweet]

    if found_items:
        print("Найдено:")
        for sweet in found_items:
            print(f"- {sweet}")
    else:
        print("Ничего не найдено.")


def delete_sweet():
    show_sweets()

    if not sweets:
        return

    choice = input("\nВведите номер сладости для удаления: ").strip()

    if not choice.isdigit():
        print("Нужно ввести номер.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(sweets):
        print("Такого номера нет.")
        return

    removed = sweets.pop(index)
    print(f"Удалено: {removed}")


def main():
    while True:
        print("\nМагазин сладостей")
        print("1. Просмотр списка сладостей")
        print("2. Добавление сладости")
        print("3. Поиск сладости по названию")
        print("4. Удаление сладости")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_sweets()
        elif choice == "2":
            add_sweet()
        elif choice == "3":
            find_sweet()
        elif choice == "4":
            delete_sweet()
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
