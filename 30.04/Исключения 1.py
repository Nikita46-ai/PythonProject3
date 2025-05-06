def main():
    while True:
        try:
            print("Введите два числа")
            a = float(input())
            b = float(input())
            print(a/b)
            break
        except ValueError:
            print("деление разных типов данных")
        except ZeroDivisionError:
            print("делить на 0 нельзя")
        except Exception:
            print("Произошла непредвиденная ошибка")
while True:
    main()














