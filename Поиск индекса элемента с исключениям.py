def find_index():
    numbers = input("Введите числа через пробел: ").split()
    if not numbers:
        raise ValueError("Список пуст")
    try:
        numbers = [int(num) for num in numbers]
    except ValueError as e:
        print("Некорректный элемент:", num)
        return
    element = int(input("Введите элемент для поиска: "))
    for index in range(len(numbers)):
        if numbers[index] == element:
            print("Индекс элемента:", index)
            return
    raise ValueError("Элемент не найден")
find_index()


