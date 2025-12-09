"""
Калькулятор с меню выбора
Лабораторная работа по Git
"""

def display_menu():
    """Отображение меню"""
    print("\n" + "="40)
    print("К А Л Ь К У Л Я Т О Р")
    print("="40)
    print("1. Ввести число A")
    print("2. Ввести число B")
    print("3. Выполнить операцию '+'")
    print("4. Выполнить операцию '-'")
    print("5. Выполнить операцию ''")
    print("6. Выполнить операцию '/'")
    print("7. Показать текущие значения")
    print("0. Выход")
    print("="40)

def main():
    """Основная функция программы"""
    a = None
    b = None

    while True:
        display_menu()
        choice = input("Выберите пункт меню (0-7): ").strip()

        if choice == '0':
            print("Выход из программы...")
            break
        elif choice == '1':
            print("Функционал ввода A будет реализован позже")
        elif choice == '2':
            try:
                b = float(input("Введите число B: "))
                print(f"Число B успешно установлено: {b}")
            except ValueError:
                print("Ошибка! Введите числовое значение.")
        elif choice == '3':
            result = add_numbers(a, b)
            if result is not None:
                print(f"Результат сложения: {a} + {b} = {result}")
        elif choice == '4':
            result = subtract_numbers(a, b)
            if result is not None:
                print(f"Результат вычитания: {a} - {b} = {result}")
        elif choice == '5':
            result = multiply_numbers(a, b)
            if result is not None:
                print(f"Результат умножения: {a} * {b} = {result}")
        elif choice == '6':
            result = divide_numbers(a, b)
            if result is not None:
                print(f"Результат деления: {a} / {b} = {result}")
        elif choice == '7':
            print(f"Текущие значения: A = {a}, B = {b}")
        else:
            print("Неверный выбор. Попробуйте снова.")
    print("Программа завершена.")

if name == "main":
    main()
