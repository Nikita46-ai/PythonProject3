def find_second_max():
    numbers = input("Введите числа через пробел: ").split()
    if len(numbers) < 2:
        raise ValueError("Список слишком мал")
    valid_numbers = []
    for num in numbers:
        try:
            valid_numbers.append(int(num))
        except ValueError:
            print("Некорректный элемент:", num)
    unique_numbers = list(set(valid_numbers))
    unique_numbers.sort()
    second_max = unique_numbers[-2]
    print("Второй по величине элемент:", second_max)
try:
    find_second_max()
except ValueError as e:
    print(e)